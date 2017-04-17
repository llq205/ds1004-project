#!/usr/bin/env python
"""
    
    map_park_name.py
    new york park names
    """
import sys
from csv import reader
col = 6
#dict = ['front of','inside','opposite of','outside','rear of']
data = reader(sys.stdin)
next(data)
for raw_cols in data:
    if raw_cols[col] == '':
        key = 'N/A'
        _time = 'N/A'
        _type = 'N/A'
        _col_name = 'key code'
        _valid = 'NULL'
    else:
        try:
            key = str(int(raw_cols[col]))
            _time = key
            _type = 'INT'
            _col_name = 'key code'
            _valid = 'VALID'
        except (TypeError, ValueError):
            key = (raw_cols[col])
            _time = key
            _type = 'STRING'
            _col_name = 'key code'
            _valid = 'INVALID'
    print ("{0:s}\t{1:s},{2:s},{3:s},{4:s}".format(key, _time, _type, _col_name, _valid))
