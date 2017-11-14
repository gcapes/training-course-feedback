% Load responses to RIT training course feedback questionnaire
% Clean and process data
% Make summary plots

loadfeedback
cleancategories
getstaffstudent
% Split VCS responses
vcs = splitmulti(feedback,'vcs',{'None','Git','Subversion','Mercurial'});
softEng = splitmulti(feedback,'softEng',{'None','Comments','Subprograms',' Assertions','Unit testing','Code reviews','Defensive programming'});
plotsummary