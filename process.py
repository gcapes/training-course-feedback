#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 26 14:18:52 2017

@author: mbexegc2
"""

import csv

csvfile=open('/home/mbexegc2/Downloads/Research IT course application.csv')
contents=csv.reader(csvfile)

# Assert to check which column headers respond to which column number
contentlist=list(contents)
print(contentlist[0][8])

for row in contentlist:
    if row[7]=='None' and row[4]!='Version control with Git and GitHub':
        print(row[2])