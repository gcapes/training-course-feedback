% Duplicate entries which have multiple responses for the specified field
	% Form allows multiple choice, including free-form 'other' option.
	% Make a duplicate entry for such responses in order to make a
	% histogram.
function outTable = splitMulti(inputTable,field)
	% Identify multiple responses
	vcs = inputTable.(field);
	isMultiResponse = ~cellfun(@isempty,regexpi(vcs,','));
	
	% Make a copy of the input data, excluding mutliple responses
	outTable = inputTable(~isMultiResponse,:);
	
	% Split multiple responses into individual single responses
	multiResponse = inputTable(isMultiResponse,:);
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