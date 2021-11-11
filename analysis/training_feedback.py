import pandas as pd
import matplotlib.pyplot as plt
import re
import streamlit as st

pd.options.mode.chained_assignment = None


def load_data():
    colHeaders = ['timeStamp','fullName','email','faculty','promo','languages','vcs','softEng','course','rating']
    colsToLoad = list(range(0,9))
    colsToLoad.append(13)
    data = pd.read_csv('feedback.tsv', delimiter='\t', usecols=colsToLoad, names=colHeaders, skiprows=1)
    return data

def clean_data(data):
    data.faculty = pd.Categorical(data.faculty)
    data.faculty = data.faculty.cat.rename_categories(['BMH', 'Hum', 'PSS', 'EPS'])
    data.rating = pd.Categorical(data.rating)
    data.rating = data.rating.cat.rename_categories([1,2,3,4,5])
    data = simple_course_names(data)
    return data


def simple_course_names(data):
    data['course'].loc[data['course'] == 'Automation and Make'] = 'Make'
    data['course'].loc[data['course'] == 'Data analysis using R'] = 'R'
    data['course'].loc[data['course'] == 'Introduction to HPC using CSF'] = 'CSF'
    data['course'].loc[data['course'] == 'Data visualisation and analysis'] = 'Vis'
    data['course'].loc[data['course'] == 'Introduction to HPC (using CSF and DPSF)'] = 'CSF'
    data['course'].loc[data['course'] == 'Introduction to LaTeX'] = 'LaTeX'
    data['course'].loc[data['course'] == 'Introduction to MATLAB'] = 'MATLAB'
    data['course'].loc[data['course'] == 'Introduction to Mathematica'] = 'Mathematica'
    data['course'].loc[data['course'] == 'Introduction to Python'] = 'Python'
    data['course'].loc[data['course'] == 'Introduction to iCSF & CSF'] = 'iCSF'
    data['course'].loc[data['course'] == 'Introduction to the UNIX shell'] = 'old Shell'
    data['course'].loc[data['course'] == 'Programming in MATLAB'] = 'old MATLAB'
    data['course'].loc[data['course'] == 'Programming in Python'] = 'Python pro'
    data['course'].loc[data['course'] == 'UNIX shell (Linux command line)'] = 'Shell'
    data['course'].loc[data['course'] == 'Version control with Git and GitHub'] = 'Git'

    return data


def course_rating_groupby(data, groupby, filter=[]):
    # Plot rating by faculty
    # unstack() gives grouped, coloured bars.
    # sort_index() sets the order of the x-axis categories
    # .T gives transpose matrix, so the plot is grouped by rating
    if filter:
        data = data.loc[data[groupby].isin(filter)]

    fig, ax = plt.subplots()
    bars = data.groupby(groupby).rating.value_counts(normalize=True).unstack().sort_index().T
    bar_labels = list(bars.columns)
    rating_labels = list(bars.index)
    ax.bar(bar_labels, bars.iloc[0], label=rating_labels[0])
    previous_row = bars.iloc[0]
    for index, row in bars.iloc[1:].iterrows():
        ax.bar(bar_labels, row, bottom=previous_row, label=index)
        previous_row += row

    ax.set_xlabel(groupby)
    ax.set_ylabel('Probability')
    ax.legend(title='Rating', loc=1, fontsize='small', fancybox=True)
    ax.set_ylim(ymax=1.0)
    plt.tight_layout()
    st.pyplot(fig)


def vcs_use_by_faculty(data):
    # Copy original (cleaned) data
    data_copy = data.copy()

    # Separate single and multiple answers into new data frames
    is_multi = data_copy['vcs'].str.contains(',')
    vcs_multi = data_copy[is_multi]
    vcs_single = data_copy[~is_multi]

    # Split multiple responses into individual single responses
    split_df = pd.DataFrame(data=None, columns=data_copy.columns)
    vcs_individual = pd.DataFrame(data=None, columns=data_copy.columns)

    for index, row in enumerate(vcs_multi.vcs):
        answers = re.split('\s*,\s*', row)
        n_answers = len(answers)
        original_row = list(vcs_multi.iloc[index])

        for i in range(0, n_answers):
            split_df.loc[i] = original_row
            # Replace multi-responses with individual
            split_df.loc[i].vcs = answers[i]
        vcs_individual = pd.merge(vcs_individual, split_df, how='outer')
    vcs_separated = pd.merge(vcs_single, vcs_individual, how='outer')

    vcs_categories = ['Git', 'None', 'Subversion', 'CVS', 'Mercurial']
    # Reclassify historic free-form answers as None (because that's what they mostly boiled down to)
    vcs_separated['vcs'].loc[~vcs_separated['vcs'].isin(vcs_categories)] = 'None'
    # Plot VCS by faculty
    ax = vcs_separated.groupby('faculty').vcs.value_counts(normalize=True).unstack().T.sort_index().plot(kind='bar', rot=0,
                                                                                                        title='Version control software')
    ax.set_xlabel('Software')
    ax.set_ylabel('Probability')
    ax.legend()
    plt.show()
    # st.pyplot()

data = load_data()
data = clean_data(data)

list_courses = list(sorted(data.course.unique()))
list_faculties = list(sorted(data.faculty.unique()))

course_rating_groupby(data, 'faculty')
course_rating_groupby(data, 'course', filter=list_courses)
vcs_use_by_faculty(data)
