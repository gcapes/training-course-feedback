isStaff = cellfun(@isempty,regexpi(feedback.email,'@postgrad'));
staffCat = strings(size(isStaff));
staffCat(~isStaff) = 'Student';
staffCat(isStaff) = 'Staff';
staffCat = table(categorical(staffCat),'VariableNames',{'status'});
feedback = [feedback,staffCat];