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

col = 1
data = reader(sys.stdin)
next(data)
for raw_cols in data:
    #key = raw_cols[0]
    try:
        time = datetime.strptime(raw_cols[col], "%m/%d/%Y").date()
        key = str(time.year)
        _time = str(time)
        _type = 'DATETIME'
        _col_name = 'date'
#        if datetime.strptime(raw_cols[1],"%m/%d/%Y").date() > datetime.strptime(raw_cols[3],"%m/%d/%Y").date():
#            _valid = 'INVALID'
        if datetime.strptime(raw_cols[col],"%m/%d/%Y").date().year<1900:
            _valid = 'INVALID'
        elif datetime.strptime(raw_cols[col],"%m/%d/%Y").date().year>2017:
            _valid = 'INVALID'
        else:
            _valid = 'VALID'
        print ("{0:s}\t{1:s},{2:s},{3:s},{4:s}".format(key, _time, _type, _col_name, _valid))
    
    except (TypeError, ValueError):
        if raw_cols[col]=='':
            key = 'NULL'
            _time = raw_cols[col]
            _type = 'DATETIME'
            _col_name = 'date'
            _valid = 'NULL'
            print ("{0:s}\t{1:s},{2:s},{3:s},{4:s}".format(key, _time, _type, _col_name, _valid))
        else:
            key = 'INVALID'
            _time = raw_cols[col]
            _type = 'DATETIME'
            _col_name = 'date'
            _valid = 'INVALID'
            print ("{0:s}\t{1:s},{2:s},{3:s},{4:s}".format(key, _time, _type, _col_name, _valid))