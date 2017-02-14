# Strip html from training catalogue's ".xls" file, and convert to csv
# Only return headers and data.

#import fileinput
import re

def attendance_list(file):
    attendance = open(file)
    data = attendance.readlines()
    feedback=[]
    
    # Lines 0-7 are headers etc 
    for line in data[8:]:
        # Skip lines which only contain html
        if '<tr>\n' or '</table>' or '</div>' not in line:
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
            
            linelist=line.split(',')
            if len(linelist) > 1 :
                # Split string into separate comma-separated items
                feedback.append(linelist)

    attendance.close()
          
    return feedback