#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 26 14:18:52 2017

@author: mbexegc2
"""
import sys
import csv

# Accept command line arguments for flexibility of file name and location
# Check there is only one argument
assert len(sys.argv)==2, "Wrong number of command line arguments"

inputfile=sys.argv[1]
csvfile=open(inputfile)
contents=list(csv.reader(csvfile))

# Check column headers of interest haven't changed
timecol=0
emailcol=2
coursecol=3
vcscol=8
assert contents[0][timecol]=="Timestamp"
assert contents[0][emailcol]=="University Of Manchester email address"
assert contents[0][coursecol]=='Which course are you applying to?'
assert contents[0][vcscol]=='Which version control systems do you use?'

for row in contentlist:
    if row[vcscol]=='None' and row[coursecol]!='Version control with Git and GitHub':
        print(row[2])

# Check for duplicates