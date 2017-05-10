#!/usr/bin/env python

#map function for checking PREM_TYP_DESC column
import os
import sys
import string
import csv

f = csv.reader(sys.stdin)
next(f)
for entry in f:
    if entry[16] == '':
        key = 'NONE'
        print "%s\t%s" % (key, 1)
    else:
        key = entry[16]
        print "%s\t%s" % (key, 1)
