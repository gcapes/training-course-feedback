% Make duplicate entries with categorical values, from input field
% consisting of a string value representing multiple responses chosen.
	% The feedback form allows multiple choice, including free-form 'other' option.
	% Make a duplicate entry for such responses in order to make a
	% histogram.
function outTable = splitMulti(inputTable,field)
	% intputTable.field should be of class string
	
	% Identify multiple responses
	vcs = inputTable.(field);
	isMultiResponse = ~cellfun(@isempty,regexpi(vcs,','));
	
	% Make a copy of the input data, excluding mutliple responses
	outTable = inputTable(~isMultiResponse,:);
	
	% Save simple responses where only one option was chosen
	multiResponse = inputTable(isMultiResponse,:);
	
	% Split multiple responses into individual single responses
	individualResponses = table;
	for row = 1:height(multiResponse)
		rowData = multiResponse(row,:);
		answers = strsplit(multiResponse.(field)(row),', ');
		splitResponse = repmat(rowData,length(answers),1);
		splitResponse.(field) = answers(:);
		individualResponses = vertcat(individualResponses,splitResponse);
	end
	outTable = vertcat(outTable,individualResponses);
	outTable.vcs = categorical(outTable.vcs,{'None','Git','Subversion', ...
		'Mercurial'});
end