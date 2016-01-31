#!/bin/python

fname = raw_input('Enter the file name: ')
if len(fname) < 1 : fname = "mbox-short.txt"
try:
    fhand = open(fname, 'r')
except:
    print 'Python was unable to open the file %s' % fname
    exit()

dic = dict()

for line in fhand:
    if not line.startswith('From '): continue
    line = line.split()
    word = line[1]
    dic[word] = dic.get(word, 0) + 1

print dic
