# Strip html from training catalogue's ".xls" file, and convert to csv
# Only return headers and data.

#import fileinput
import re

def attendance_list(file):
    attendance = open(file)
    data = attendance.readlines()
    feedback=[]

    for line in data:
#        if line.strip():
        # Strip end of line character
        line = line.rstrip()
        # Strip leading whitespace
        line = re.sub('^\s+','',line)
        # Strip adjacent html tags
        line = re.sub('(<.+?>){2}',';',line)
        # Replace html tag with comma
        line = re.sub('<.+?>',';',line)
        # Remove html
        line = re.sub('&\w+;','',line)
        # Strip leading semi-colons
        line = re.sub('^;+','',line)
        # Strip trailing semi-colons
        line = re.sub(';+$','',line)
        # Strip adjacent semi-colons
        line = re.sub(';{2,5}','',line)
        # Strip commas
        line = re.sub(',','',line)
        # Replace semi-colons with commas
        line = re.sub(';',',',line)
#        linelist=list(line)
        if len(line)>0:
            feedback.append(line.split(','))

    attendance.close()
          
    return feedback