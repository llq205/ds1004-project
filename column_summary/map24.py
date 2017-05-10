#!/usr/bin/env python

#map function for checking coordinates column 
import os
import sys
import string
import csv

f = csv.reader(sys.stdin)
next(f)
for entry in f:
    if entry[-1] == '' and entry[-2] == '' and entry[-3] == '':
        key = 'NONE'
        print "%s\t%s" % (key, 1)
    else:
        a, b = entry[-1][1:-1].split(',')
        if round(float(a),5) == round(float(entry[-3]), 5) and round(float(b),5) == round(float(entry[-2]), 5) and abs(float(entry[-3])) > 39 and abs(float(entry[-3])) < 42 and abs(float(entry[-2])) > 72 and abs(float(entry[-2])) < 75:
            key = 'VALID'
            print "%s\t%s" % (key, 1)
        else:
            key = 'INVALID'
            print "%s\t%s" % (key, 1)
