#!/bin/python

import string

fname = raw_input('Enter the file name: ')
if len(fname) < 1 : fname = 'romeo-full.txt'
try:
    fhand = open(fname, 'r')
except:
    print 'Python was unable to open the file %s' % fname
    exit()

counts = dict()

for line in fhand:
  line = line.translate(None, string.punctuation)
  line = line.lower()
  words = line.split()
  for word in words:
    if word not in counts:
        counts[word] = 1
    else:
        counts[word] += 1

# Sort the dictionary by value
lst = list()
for key, val in counts.items():
    lst.append( (val, key) )
    lst.sort(reverse=True)
for key, val in lst[:10] :
    print key, val
