#!/usr/bin/env python

#Reduce function for checking year

import sys
import string


current_year = None
current_count = 0
year = None
# input comes from STDIN (stream data that goes to the program)
for line in sys.stdin:

    #Remove leading and trailing whitespace
    line = line.strip()
    year, count = line.split('\t',1)

    try:
        count = int(count)
    except ValueError:
        continue
        
        
    if current_year == year:
        current_count += count
    else:
        if current_year:
            # write result to STDOUT
            print '%s\t%s' % (current_year, current_count)
        current_count = count
        current_year = year

print '%s\t%s' % (current_year, current_count)
