#!/usr/bin/env python

#Reduce function for checking month

import sys
import string


current_month = None
current_count = 0
month = None
# input comes from STDIN (stream data that goes to the program)
for line in sys.stdin:

    #Remove leading and trailing whitespace
    line = line.strip()
    month, count = line.split('\t',1)

    try:
        count = int(count)
    except ValueError:
        continue
        
        
    if current_month == month:
        current_count += count
    else:
        if current_month:
            # write result to STDOUT
            print '%s\t%s' % (current_month, current_count)
        current_count = count
        current_month = month

print '%s\t%s' % (current_month, current_count)
