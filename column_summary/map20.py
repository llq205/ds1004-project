#!/usr/bin/env python

#map function for checking column 'HADEVELOPT'
import os
import sys
import string
import csv

f = csv.reader(sys.stdin)
next(f)
for entry in f:
    if entry[-6] == '':
        key = 'NONE'
        print "%s\t%s" % (key, 1)
    else:
        key = 'VALID'
        print "%s\t%s" % (key, 1)

