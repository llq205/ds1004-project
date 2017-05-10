#!/usr/bin/env python

#map function for checking time(hour)
import os
import sys
import string
import csv

f = csv.reader(sys.stdin)
next(f)
for entry in f:
    if entry[4] == '':
        key = 'NONE'
        print "%s\t%s" % (key, 1)
    else:
        key = entry[4][0:2]
        print "%s\t%s" % (key, 1)

