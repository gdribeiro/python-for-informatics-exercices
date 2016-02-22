#!/bin/python


import string


fname = raw_input('Enter the file name: ')
if len(fname) < 1 : fname = 'mbox.txt'

try:
    fhand = open(fname, 'r')
except:
    print 'There was a problem while opening the file %s' % fname
    exit()

ddd = dict()

for line in fhand:
    if not line.startswith('From '): continue
    line = line.strip()
    line = line.split()
    word = line[1]
    ddd[word] = ddd.get(word, 0) + 1

lst = list()

for key, val in ddd.items():
    # Creates a list of tuples with the value, key order
    lst.append( (val,key) )

lst.sort(reverse=True)

for item in lst[:10]:
    print item 
