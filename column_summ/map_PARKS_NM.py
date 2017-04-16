#!/usr/bin/env python
"""
    
    map_park_name.py
    new york park names
    """
import sys
from csv import reader
col = -7
#dict = ['front of','inside','opposite of','outside','rear of']
data = reader(sys.stdin)
next(data)
for raw_cols in data:
    if raw_cols[col] == '':
        key = 'N/A'
        _time = raw_cols[col]
        _type = 'STRING'
        _col_name = 'park names'
        _valid = 'NULL'
    else:
        key = raw_cols[col]
        _time = raw_cols[col]
        _type = 'STRING'
        _col_name = 'park names'
        _valid = 'VALID'
    print ("{0:s}\t{1:s},{2:s},{3:s},{4:s}".format(key, _time, _type, _col_name, _valid))