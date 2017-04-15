#!/usr/bin/env python

#map function for task 1

import sys
import string
import csv

key = ''
picked_column = None
type = 'float'
label = None
descr = 'PD_CD'
lines = csv.reader(sys.stdin)

for entry in lines:
    key = entry[0]
    picked_column = entry[8]
    if picked_column is None or picked_column == 'NaN' or picked_column == '':
        label = 'NULL'
        type = 'NULL'
    else:
        try:
            picked_column = float(picked_column)
            label = 'VALID'
        except ValueError:
            label = 'INVALID'
    #type = picked_column.type
    print '%s,%s,%s,%s' % (key,type,descr,label)
