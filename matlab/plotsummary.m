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
xlabel('Software')
saveas(gcf,'vcsByFaculty.png')

%% Rating by faculty
ratingCats = categorical(categories(feedback.rating));
ratingProb = [];
for i = 1:length(facultyCats)
	faculty = facultyCats(i);
	ratingProbByFac(:,i) = histcounts(feedback.rating(feedback.faculty==faculty),'Normalization','pdf');
end

% Create categorical array for plotting against
ratingCats = categorical(categories(feedback.rating));
	
% Plot bar chart
bar(ratingCats,ratingProbByFac)
legend(string(facultyCats),'Location','northwest')
title('Course rating by faculty')
ylabel('Probability')
xlabel('Rating (1 - 5)')
saveas(gcf,'ratingByFaculty.png')

%% Rating by course
courseList = categorical(categories(feedback.course));
ratingProbByCourse=[];
for i = 1:length(courseList)
	course = courseList(i);
	ratingProbByCourse(:,i)= histcounts(feedback.rating(feedback.course==course),'Normalization','pdf');
end

% Plot bar chart
bar(ratingCats,ratingProbByCourse);
colormap jet
legend(string(courseList),'Location','NorthWest')
title('Rating by course')
ylabel('Probability')
xlabel('Rating (1 - 5)')
saveas(gcf,'ratingByCourse.png')

%% Software Engineering by faculty
softEngCats = categorical(categories(softEng.softEng));
softEngProb = [];
for i = 1:length(facultyCats)
	faculty = facultyCats(i);
	softEngProb(:,i) = histcounts(softEng.softEng(softEng.faculty==faculty),'Normalization','pdf');
end

bar(softEngCats,softEngProb)
title('Software Engineering techniques used by faculty')
legend(string(facultyCats),'Location','NorthWest')
xlabel('Technique')
ylabel('Probability')
saveas(gcf,'softEngByFaculty.png')