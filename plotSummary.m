%% Version Control by faculty
% Generate summary statistics
facultyCats = categorical(categories(vcs.faculty));
vcsProb = [];
for i = 1:length(facultyCats)
	faculty = facultyCats(i);
	vcsProb(:,i) = histcounts(vcs.vcs(vcs.faculty==faculty),'Normalization','pdf');
end

% Create categorical array for plotting against
vcsCats = categorical(categories(vcs.vcs));

% Plot results
bar(vcsCats,vcsProb)
legend(string(facultyCats))
title('VCS usage by faculty')
ylabel('Probability')
saveas(gcf,'vcsByFaculty.png')