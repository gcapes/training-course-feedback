% Split VCS responses
vcs = splitMulti(feedback,'vcs');

% Generate summary statistics
vcsCounts = histcounts(vcs.vcs(vcs.faculty=='EPS'));
vcsCounts(2,:)=histcounts(vcs.vcs(vcs.faculty=='BMH'));
vcsCounts(3,:)=histcounts(vcs.vcs(vcs.faculty=='Hum'));
vcsCounts(4,:)=histcounts(vcs.vcs(vcs.faculty=='PSS'));

% Transpose for bar plot
vcsCounts = vcsCounts.';
vcsCats = categorical(categories(vcs.vcs));

% Plot results
bar(vcsCats,vcsCounts,'stacked')
legend('EPS','BMH','Hum','PSS')
title('VCS usage by faculty')
ylabel('Frequency')
