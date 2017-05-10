#!/usr/bin/env python

#Reduce function for checking time(hour)

import sys
import string


current_hour = None
current_count = 0
hour = None
# input comes from STDIN (stream data that goes to the program)
for line in sys.stdin:

    #Remove leading and trailing whitespace
    line = line.strip()
    #print(line.split('\t',1))
    hour, count = line.split('\t',1)

    try:
        count = int(count)
    except ValueError:
        continue
        
        
    if current_hour == hour:
        current_count += count
    else:
        if current_hour:
            # write result to STDOUT
            print '%s\t%s' % (current_hour, current_count)
        current_count = count
        current_hour = hour

print '%s\t%s' % (current_hour, current_count)
