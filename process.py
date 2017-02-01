# Script to process applications to moderated Research IT courses
    # Download the responses to the google forms questionnaire
    # Call the script with two arguments, the csv file and the archived responses
    # Script returns a list of people who don't use version control
    # Email them to advertise Git course
import sys
import os
import csv
import shutil

# Accept command line arguments for flexibility of file name and location
# Check there are two arguments
assert len(sys.argv)==3, "Two arguments required: <currentfile.csv> <archivefile.csv>"

inputfile=sys.argv[1]
csvfile=open(inputfile)
contents=list(csv.reader(csvfile))

# Check column headers of interest haven't changed
timecol=0
emailcol=2
coursecol=3
vcscol=8
assert contents[0][timecol]=="Timestamp"
assert contents[0][emailcol]=="University Of Manchester email address"
assert contents[0][coursecol]=='Which course are you applying to?'
assert contents[0][vcscol]=='Which version control systems do you use?'

# Check for updates to file
archivefilename=sys.argv[2]
if os.path.isfile(archivefilename):
    # Archive file exists
    archivefile=open(archivefilename)
    archivedata=list(csv.reader(archivefile))
    if len(archivedata)<len(contents):
        # There is new data to process
        startrow=len(archivedata)
else:
    # Archive file doesn't exist, so process all data
    startrow=0

needsgit=[]

# If there is data to process, startrow should exist
if 'startrow' in locals():
    for row in contents[startrow:]:
        if row[vcscol]=='None' \
            and row[coursecol]!='Version control with Git and GitHub'\
            and '@' in row[emailcol]: # Check email address has been entered
            needsgit.append(row[2])
    if len(needsgit)>0:
        # Remove duplicates
        needsgit=set(needsgit)

        # Now process the needsgit list to remove entries with a subsequent
        # application to the Git course
        for row in contents[startrow:]:
            if row[coursecol]=='Version control with Git and GitHub'\
                and row[emailcol] in needsgit:
                needsgit.remove(row[emailcol])


# Whether or not there are any matches, print output and update files.
# This enables use of a makefile.
print('%i people for Git course promotion' % len(needsgit))    

# Save email addresses to file
emails=csv.writer(open('emailgitpromo.csv','w'))
emails.writerow(list(needsgit))

# Overwrite archive with current file
shutil.copyfile(inputfile,archivefilename)
