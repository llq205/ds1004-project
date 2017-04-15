#!/usr/bin/env python

#map function for task 1

import sys
import string
import csv

key = ''
picked_column = None
type = 'string'
label = None
descr = 'OFNS Description'
lines = csv.reader(sys.stdin)

for entry in lines:
    key = entry[0]
    picked_column = entry[7]
    if picked_column == None or picked_column == 'nan' or picked_column == '':
        label = 'NULL'
        type = 'NULL'
    else:
        try:
            picked_column = str(picked_column)
            label = 'VALID'
        except ValueError:
            label = 'INVALID'
    #type = picked_column.type
    print '%s,%s,%s,%s' % (picked_column,type,descr,label)
