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
    splitDF = pd.DataFrame(data=None, columns=vcs.columns)
    dropRows = []

    for i, row in enumerate(vcs.vcs):
        splitRow = re.split('\s*,\s*', row)
        nAnswers = len(splitRow)
        originalRow = list(vcs.iloc[i])

        if nAnswers > 1:
            # Append split up responses to data frame.
            for answer in splitRow:
                dropRows.append(i)
                currentRow = len(splitDF)

                # Append original row to dataframe
                splitDF.loc[currentRow] = originalRow

                # Replace vcs in current row with each answer in turn
                splitDF = splitDF._set_value(currentRow, 'vcs', answer)

    # Delete original rows
    vcs.drop(vcs.index[dropRows], inplace=True)

    # Join data frames
    # new = pd.concat([vcs, splitDF], axis=0, ignore_index=True)
    new = pd.merge(vcs, splitDF, how='outer')

    assert (new.shape[0] == vcs.shape[0] + splitDF.shape[0])

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
course_rating_by_faculty(data)
