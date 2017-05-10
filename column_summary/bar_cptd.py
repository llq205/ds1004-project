#!/usr/bin/env python

#Reduce function for task2

import sys
import string


cn = 'BORO_NM'
key = '-'
#unique_value = 0
#miss = 0
base_type = 'string'
semantic_type = '-'
valid = 0
invalid = 0
nu = 0
label = '-'
CP = 0
AT = 0
name = 'COUNT'

# input comes from STDIN (stream data that goes to the program)
for line in sys.stdin:

    #Remove leading and trailing whitespace
    line = line.strip()

    #Get key/value 
    key,bas_type,semantic_type,label=line.split(',',3)
    #print label
    
    if label == 'VALID':
        valid += 1
    elif label == 'INVALID':
        invalid += 1 
    else:
        nu += 1
    
    if key == 'COMPLETED':
        CP += 1
    if key == 'ATTEMPTED':
        AT += 1

print 'CPTD\tCOMPLETED, ATTEMPTED, NULL'   
print '%s\t%s, %s, %s' %(name,CP,AT,nu)
