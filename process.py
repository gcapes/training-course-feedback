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
contents=csv.reader(csvfile)

# Assert to check which column headers respond to which column number
contentlist=list(contents)
print(contentlist[0][8])

for row in contentlist:
    if row[7]=='None' and row[4]!='Version control with Git and GitHub':
        print(row[2])