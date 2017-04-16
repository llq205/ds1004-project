#!/usr/bin/env python

"""
    map.py time data
    Author: Yurui Mu
    key = complaint_id
    values = date, data_type, col_name, valid/invalid/null
    """

import sys
from csv import reader
from datetime import datetime

col = 2
data = reader(sys.stdin)
next(data)
for raw_cols in data:
    key = raw_cols[0]
    try:
        time = datetime.strptime(raw_cols[col], "%H:%M:%S").time()
        _time = str(time)
        _type = 'DATETIME'
        _col_name = 'time'
        _valid = 'VALID'
        print ("{0:s}\t{1:s},{2:s},{3:s},{4:s}".format(key, _time, _type, _col_name, _valid))
    
    except (TypeError, ValueError):
        if raw_cols[col]=='':
            _time = raw_cols[col]
            _type = 'DATETIME'
            _col_name = 'time'
            _valid = 'NULL'
            print ("{0:s}\t{1:s},{2:s},{3:s},{4:s}".format(key, _time, _type, _col_name, _valid))
        else:
            _time = raw_cols[col]
            _type = 'DATETIME'
            _col_name = 'time'
            _valid = 'INVALID'
            print ("{0:s}\t{1:s},{2:s},{3:s},{4:s}".format(key, _time, _type, _col_name, _valid))