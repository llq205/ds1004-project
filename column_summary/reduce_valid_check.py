#!/usr/bin/env python

#Reduce function to check valid/invalid/null

import sys
import string


current_valid = 0
current_invalid = 0
current_null = 0
current_count = 0
# input comes from STDIN (stream data that goes to the program)
for line in sys.stdin:
    current_count  = current_count+1
    #Remove leading and trailing whitespace
    line = line.strip()
    #print(line.split('\t',1))
    _id,_rest  = line.split('\t',1)
    _value, _type, _col_name, _valid = _rest.split(',',3)
    if _valid =='VALID':
        current_valid = current_valid+1
    elif _valid =='INVALID':
        current_invalid = current_invalid+1
    else:
        current_null = current_null+1
print"{0:s}\t{1:d},{2:.4f}".format('VALID', current_valid, float(current_valid)/float(current_count))
print"{0:s}\t{1:d},{2:.4f}".format('INVALID', current_invalid, float(current_invalid)/float(current_count))
print"{0:s}\t{1:d},{2:.4f}".format('NULL', current_null, float(current_null)/float(current_count))