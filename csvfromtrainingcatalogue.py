# Strip html from training catalogue's ".xls" file, and convert to csv
# Only return headers and data.

import re

def attendance_list(file):
    attendance = open(file)
    data = attendance.readlines()
    feedback=[]
    
    # Lines 0-7 are headers etc 
    for line in data[8:]:
        # Skip lines which only contain html
        if ('<tr>\n' not in line) and ('</table>' not in line) and ('</div>' not in line):
            # html tag for table cell is <td>...</td>
            # Strip start of cell tags
            line = re.sub('<td>','',line)
            # Strip final end of cell tag on line
            line = re.sub('</td>\n','',line)
            # Replace end of cell tags with commas
            line = re.sub('</td>',',',line)
            # Strip leading whitespace
            line = re.sub('^\s+','',line)
            # Strip non-breaking spaces
            line = re.sub('&nbsp;','',line)
            
	    # Split string into separate comma-separated items
            linelist=line.split(',')

            # Only interested in first 9 columns:
            # comment column isn't treated well by the above regex,
            # because it can contain new lines.
            if len(linelist) >= 10 :
                feedback.append(linelist[:10])

    attendance.close()
          
    return feedback
