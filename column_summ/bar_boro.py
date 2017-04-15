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
BR = 0
QU = 0
MH = 0
BK = 0
SI = 0


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
    
    if key == 'BRONX':
        BR += 1
    if key == 'QUEENS':
        QU += 1
    if key == 'MANHATTAN':
        MH += 1
    if key == 'BROOKLYN':
        BK += 1
    if key == 'STATEN ISLAND':
        SI += 1
   
print '%s\t%s, %s, %s, %s, %s, %s' %(key,BR,QU,MH,BK,SI,nu)
