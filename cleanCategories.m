% Combine categories whose names have changed over time
oldCats = {'StaffNet Learning and Development page', ...
	'Staffnet (staffnet.manchester.ac.uk/employment/training/it-systems/research-computing/research-courses/)' ...
	'Staffnet Learning and Development page (http://www.staffnet.manchester.ac.uk/staff-learning-and-development/academicandresearch/practical-skills-and-knowledge/it-skills/research-computing/research-courses/)' ...
	};
feedback.promotion = mergecats(feedback.promotion,oldCats);

% Merge individual responses from 'other' category
simpleCats = {'StaffNet Learning and Development page',...
	'A University email list','Research IT newsletter (researchitnews.org)', ...
	'Supervisor','Word of mouth'};

promo = feedback.promotion;
promo(promo == 'Research IT newsletter (researchitnews.org)') = 'Research IT news';
promo(promo == 'Staffnet Learning and Development page') = 'SLDU';
promo(promo == 'A University email list ') = 'Email list';

promo = setcats(feedback.promotion,simpleCats);
promo(isundefined(promo))= 'Other';
shortCats = {'SLDU','Email list','Research IT news','Supervisor',...
	'Word of mouth','Other'};
promo = renamecats(promo,shortCats);
feedback.promotion = promo;

clear promo oldCats shortCats simpleCats

% Rename categories
feedback.faculty = renamecats(feedback.faculty,{'BMH','Hum','PSS','EPS'});