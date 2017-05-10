#!/usr/bin/env python

#Reduce function for checking day in date

import sys
import string


current_day = None
current_count = 0
day = None
# input comes from STDIN (stream data that goes to the program)
for line in sys.stdin:

    #Remove leading and trailing whitespace
    line = line.strip()
    day, count = line.split('\t',1)

    try:
        count = int(count)
    except ValueError:
        continue
        
        
    if current_day == day:
        current_count += count
    else:
        if current_day:
            # write result to STDOUT
            print '%s\t%s' % (current_day, current_count)
        current_count = count
        current_day = day

print '%s\t%s' % (current_day, current_count)
