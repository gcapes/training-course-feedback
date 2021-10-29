import pandas as pd
import matplotlib.pyplot as plt
import re


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
    return data

def course_rating_groupby(data, groupby):
    # Plot rating by faculty
    # unstack() gives grouped, coloured bars.
    # sort_index() sets the order of the x-axis categories
    # .T gives transpose matrix, so the plot is grouped by rating
    ax = data.groupby(groupby).rating.value_counts(normalize=True).unstack().T.sort_index().plot(kind='bar', rot=0, title='Rating')
    ax.set_xlabel('Rating (1-5)')
    ax.set_ylabel('Probability')
    ax.legend()
    plt.show()


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


data = load_data()
data = clean_data(data)
course_rating_groupby(data, 'faculty')
course_rating_groupby(data, 'course')
vcs_use_by_faculty(data)
