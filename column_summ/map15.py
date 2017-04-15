#!/usr/bin/env python

#map function for task 1

import sys
import string
import csv

key = ''
picked_column = None
type = 'float'
label = None
descr = 'Adress Number'
lines = csv.reader(sys.stdin)

for entry in lines:
    key = entry[0]
    picked_column = entry[14]
    if picked_column == None or picked_column == 'N/A' or picked_column == '':
        label = 'NULL'
        type = 'NULL'
       # print picked_column
    else:
        try:
            picked_column = float(picked_column)
            label = 'VALID'
        except ValueError:
            label = 'INVALID'
    #type = picked_column.type
    print '%s,%s,%s,%s' % (key,type,descr,label)
