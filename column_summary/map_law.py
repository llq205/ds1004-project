#!/usr/bin/env python

#map function for task 1

import sys
import string
import csv

key = ''
picked_column = None
type = 'string'
label = None
descr = 'crime character'
lines = csv.reader(sys.stdin)

for entry in lines:
    key = entry[0]
    picked_column = entry[11]
    if picked_column == None or picked_column == 'N/A' or picked_column == '':
        label = 'NULL'
        type = 'NULL'
       # print picked_column
    else:
        try:
            picked_column = str(picked_column)
            label = 'VALID'
        except ValueError:
            label = 'INVALID'
    #type = picked_column.type
    print '%s,%s,%s,%s' % (picked_column,type,descr,label)
