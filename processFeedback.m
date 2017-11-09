% Load responses to RIT training course feedback questionnaire
% Clean and process data
% Make summary plots

loadFeedback
cleanCategories
getStaffStudent
% Split VCS responses
vcs = splitMulti(feedback,'vcs',{'None','Git','Subversion','Mercurial'});
plotSummary
softEng = splitMulti(feedback,'softEng',{'None','Comments','Subprograms',' Assertions','Unit testing','Code reviews','Defensive programming'});