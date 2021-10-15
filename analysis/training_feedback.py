import pandas as pd
import matplotlib.pyplot as plt
import re


def load_data():
    colHeaders = ['timeStamp','fullName','email','faculty','promo','languages','vcs','softEng','course','rating']
    colsToLoad = list(range(0,9))
    colsToLoad.append(13)
    data = pd.read_csv('feedback.tsv', delimiter='\t', usecols=colsToLoad, names=colHeaders, skiprows=1)
    return data


def course_rating_by_faculty(data):
    data.faculty = pd.Categorical(data.faculty)
    data.faculty = data.faculty.cat.rename_categories(['BMH','Hum','PSS','EPS'])
    data.rating = pd.Categorical(data.rating)
    data.rating = data.rating.cat.rename_categories([1,2,3,4,5])

    # Plot rating by faculty
    # unstack() gives grouped, coloured bars.
    # sort_index() sets the order of the x-axis categories
    # .T gives transpose matrix, so the plot is grouped by rating
    ax = data.groupby('faculty').rating.value_counts(normalize=True).unstack().T.sort_index().plot(kind='bar', rot=0, title='Rating')
    ax.set_xlabel('Rating (1-5)')
    ax.set_ylabel('Probability')
    plt.show()


def version_control_use_by_faculty(data):
    # Split multiple answers into separate rows
    vcs = data.copy()
    # Empty data frame to populate with split answers and merge at the end
    split_df = pd.DataFrame(data=None, columns=vcs.columns)
    drop_rows = []

    for i, row in enumerate(vcs.vcs):
        split_row = re.split('\s*,\s*', row)
        n_answers = len(split_row)
        original_row = list(vcs.iloc[i])

        if n_answers > 1:
            # Append split up responses to data frame.
            for answer in split_row:
                drop_rows.append(i)
                current_row = len(split_df)

                # Append original row to dataframe
                split_df.loc[current_row] = original_row

                # Replace vcs in current row with each answer in turn
                split_df.at[current_row, 'vcs'] = answer

    # Delete original rows
    vcs.drop(vcs.index[drop_rows], inplace=True)

    # Join data frames
    # new = pd.concat([vcs, split_df], axis=0, ignore_index=True)
    new = pd.merge(vcs, split_df, how='outer')

    assert (new.shape[0] == vcs.shape[0] + split_df.shape[0])

    ## To do:
        # - Test that all the right lines have been dropped (check against MATLAB code)
        # - Set 'vcs' column as categorical

    # Plot VCS by faculty
    ax = new.groupby('faculty').vcs.value_counts(normalize = True).unstack().T.sort_index().plot(kind = 'bar', rot = 0, title = 'Version control software')
    ax.set_xlabel('Software')
    ax.set_ylabel('Probability')
    plt.show()


## Another attempt using vectorisation and logical indexing
def vs_use_by_faculty_take_2(data):
    # Copy original (cleaned) data
    vcsVec = data.copy()

    # Separate single and multiple answers into new data frames
    isMulti = vcsVec['vcs'].str.contains(',')
    vcsMulti = vcsVec[isMulti]
    vcsSingle = vcsVec[~isMulti]

    # Split multiple responses into individual single responses
    splitDF = pd.DataFrame(data=None, columns=vcsVec.columns)
    vcsIndividual = pd.DataFrame(data=None, columns=vcsVec.columns)

    for index, row in enumerate(vcsMulti.vcs):
        answers = re.split('\s*,\s*', row)
        nAnswers = len(answers)
        originalRow = list(vcsMulti.iloc[index])

        for i in range(0, nAnswers):
            splitDF.loc[i] = originalRow
            # Replace multi-responses with individual
            splitDF.loc[i].vcs = answers[i]
        vcsIndividual = pd.merge(vcsIndividual, splitDF, how='outer')
    vcsSeparated = pd.merge(vcsSingle, vcsIndividual, how='outer')
    assert (new.equals(vcsSeparated))

    # Plot VCS by faculty
    ax = vcsSeparated.groupby('faculty').vcs.value_counts(normalize=True).unstack().T.sort_index().plot(kind='bar', rot=0,
                                                                                                        title='Version control software')
    ax.set_xlabel('Software')
    ax.set_ylabel('Probability')
    plt.show()


data = load_data()
# course_rating_by_faculty(data)
version_control_use_by_faculty(data)
