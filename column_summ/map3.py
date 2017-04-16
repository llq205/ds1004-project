#!/usr/bin/env python

#map function for checking day in date
import os
import sys
import string
import csv

f = csv.reader(sys.stdin)
next(f)
for entry in f:
    if entry[5] == "":
        key = 'NONE'
        print "%s\t%s" % (key, 1)
    else:    
        key = entry[5][3:5]
        print "%s\t%s" % (key, 1)

