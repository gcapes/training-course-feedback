import processfeedback

# Only advertise Git to those who don't use any version control already, and haven't
# already Attended the Git course.

# Test subjects:
    # 1-6 use only the feedback data.
# 1. Attended LaTeX course, doesn't use VCS. Result: on list.
# 2. Attended Git course. Result: not on list.
# 3. Attended Python, doesn't use VCS, also Attended Git course. Result: not on list.
# 4. Attended two courses, MATLAB and LaTeX, doesn't use VCS. Result: on list once.
# 5. Attended Python, uses VCS already. Result: not on list.
# 6. Attended MATLAB, doesn't use VCS. Then Attended Python, now does use VCS. Result: not on list.
    # 7-8 also use the git course attendance data
# 7. Attended Automation and Make, doesn't use version control, applied to Git course. Result: not on list.
# 8. Attended UNIX shell, doesn't use version control, hasn't applied to Git course. Result: on list.
# 9. Attended UNIX shell, doesn't use version control, hasn't applied to Git course, but already emailed. Result: not on list.
testdata=[
['14/10/2016 16:41:59', 'Scenario 1', 'scenario1@manchester.ac.uk', 'Typesetting your thesis with LaTeX', 'Word of mouth', 'use Latex', 'Humanities', 'None', 'None', 'None'], 
['15/10/2016 15:52:37', 'Scenario 1 Repeat', 'scenario1.repeat@manchester.ac.uk', 'Typesetting your thesis with LaTeX', "Thomas Bishop's mouth", 'er typesetting with LaTeX', 'Humanities', 'R', 'None', 'None'], 
['16/10/2016 10:02:56', 'Scenario 2', 'scenario2@manchester.ac.uk', 'Version control with Git and GitHub', 'Word of mouth', 'How to use revert.', 'Science and Engineering', 'C/C++', 'Ubuntu', 'OpenFoam'], 
['17/10/2016 08:21:03', 'Scenario 3', 'scenario3@manchester.ac.uk', 'Programming in Python', 'Word of mouth', 'functions', 'Humanities', 'Stata', 'None', 'None'], 
['17/10/2016 08:21:03', 'Scenario 3', 'scenario3@manchester.ac.uk', 'Version control with Git and GitHub', 'Word of mouth', 'Rebasing', 'Humanities', 'Stata', 'None', 'None'], 
['17/10/2016 15:29:53', 'Scenario 4', 'scenario4@manchester.ac.uk', 'Typesetting your thesis with LaTeX', 'Word of mouth', 'How can I make the most of the software', 'Science and Engineering', 'C/C++', 'None', 'Use of sub-programs (e.g. functions, subroutines, methods, procedures)'], 
['17/10/2016 15:29:53', 'Scenario 4', 'scenario4@manchester.ac.uk', 'Progamming in MATLAB', 'Word of mouth', 'How can I make the most of the software', 'Science and Engineering', 'C/C++', 'None', 'Use of sub-programs (e.g. functions, subroutines, methods, procedures)'],
['17/10/2016 16:03:02', 'Scenario 5', 'scenario5@manchester.ac.uk', 'Programming in Python', 'Word of mouth', 'General intro for Python', 'Biology, Medicine and Health', 'Python', 'Mercurial', 'Use of sub-programs (e.g. functions, subroutines, methods, procedures)'], 
['18/10/2016 08:45:26', 'Scenario 6', 'scenario6@manchester.ac.uk', 'Programming in MATLAB', 'Word of mouth', 'How to do scripts with MATLAB.', 'Science and Engineering', 'C/C++', 'None', 'Use of sub-programs (e.g. functions, subroutines, methods, procedures)'], 
['18/10/2016 08:48:19', 'Scenario 6', 'scenario6@manchester.ac.uk', 'Programming in Python', 'Staffnet (staffnet.manchester.ac.uk/employment/training/it-systems/research-computing/research-courses/)', 'Research', 'Humanities', 'C/C++', 'SVN', 'Use of sub-programs (e.g. functions, subroutines, methods, procedures)'],
['','Scenario 7','scenario7@manchester.ac.uk','Automation and Make','','','','','None'],
['','Scenario 8','scenario8@manchester.ac.uk','UNIX shell','','','','','None'],
['','Scenario 9','scenario9@manchester.ac.uk','UNIX shell','','','','','None']
]
vcscol=8
emailcol=2
coursecol=3

gitattendance=[['','','','','','','scenario7@manchester.ac.uk','','Confirmed']]
gitstatuscol=8
gitemailcol=6
gitpromoarchive=['scenario9@manchester.ac.uk']

actual=processfeedback.get_emails(testdata,vcscol,emailcol,coursecol,0,gitattendance,gitemailcol,gitstatuscol,gitpromoarchive)
actual=list(actual)
actual.sort()
expected=['scenario1@manchester.ac.uk','scenario1.repeat@manchester.ac.uk','scenario4@manchester.ac.uk','scenario8@manchester.ac.uk']
expected.sort()

assert actual==expected, "Git test FAILED.\nExpected: %r\nActual: %r" % (expected,actual)
print('Git test PASSED')
