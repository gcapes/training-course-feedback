# Script to process applications to moderated Research IT courses.
# Instructions:
    # Download the responses to the google forms questionnaire
    # Call the script with three arguments:
        # python responses.csv archive.csv, emailsforgitpromotion.csv
    # Script returns a list of people who don't use version control.
    # Email them to advertise Git course.
import sys
import os
import csv
import shutil
#import csvfromtrainingcatalogue

def check_headers(contents,timecol,emailcol,coursecol,vcscol):
    assert contents[0][timecol]=="Timestamp"
    assert contents[0][emailcol]=="University Of Manchester email address" 
    assert contents[0][coursecol]=='Which course did you attend?'
    assert contents[0][vcscol]=='Which version control systems do you use?'

def get_start_row(archivefilename):
    if os.path.isfile(archivefilename):
        # Archive file exists
        archivefile=open(archivefilename)
        archivedata=list(csv.reader(archivefile))
        # There is potentially new data to process
        startrow=len(archivedata)
    else:
        # Archive file doesn't exist, so process all data
        startrow=0

    return startrow 

def get_emails(responsedata,vcscol,emailcol,coursecol,startrow):
    needsgit=[]
    for row in responsedata[startrow:]:
        if row[vcscol]=='None' \
            and row[coursecol]!='Version control with Git and GitHub'\
            and '@' in row[emailcol]: # Check email address has been entered
            needsgit.append(row[2])
    if len(needsgit)>0:
        # Remove duplicates
        needsgit=set(needsgit)

        # Remove entries if they have started using VC or attended Git course.
        for row in responsedata[startrow:]:
            if (row[coursecol]=='Version control with Git and GitHub'\
                or row[vcscol]!='None') and row[emailcol] in needsgit:
                needsgit.remove(row[emailcol])
        # The above block really needs changing because it only processes
        # new feedback responses, rather than applications to the Git course.
        # Ideal future functionality:
            # Process the needsgit list to remove entries where a learner
            # has applied to or attended the Git course or otherwise started
            # using version control. Would obviously need to export and load
            # the Git course attendance.
#        gitattendance=csvfromtrainingcatalogue.attendance_list('gitall.xls')
#        for row in gitattendance:
#            use list indices appropriate for the gitattendance list
    return needsgit

# Run the following commands if executed as a script. Ignore if imported as module.
if __name__=="__main__":
    # Check there are three arguments
    assert len(sys.argv)==4, ("Three arguments required: "
    	"<currentresponses.csv> <archive.csv> <gitpromolist.csv>")
    
    inputfile=sys.argv[1]
    archivefilename=sys.argv[2]
    gitpromofile=sys.argv[3]
    
    csvfile=open(inputfile)
    contents=list(csv.reader(csvfile))
    
    # Check column headers of interest haven't changed
    timecol=0
    emailcol=2
    coursecol=8
    vcscol=6
    check_headers(contents,timecol,emailcol,coursecol,vcscol)
    
    # Check for updates to file
    startrow=get_start_row(archivefilename)
    
    # Get list of email addresses for Git course promotion
    needsgit=get_emails(contents,vcscol,emailcol,coursecol,startrow)
    
    # Whether or not there are any matches, print output and update files.
    # This enables use of a makefile.
    print('%i people for Git course promotion' % len(needsgit))    
    
    # Save email addresses to file
    emails=csv.writer(open(gitpromofile,'w'))
    emails.writerow(list(needsgit))
    
    # Overwrite archive with current file
    shutil.copyfile(inputfile,archivefilename)
