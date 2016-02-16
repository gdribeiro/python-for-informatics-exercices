#!/bin/python

# Exercise 8.5 - Python for Informatics

fhand = open('mbox-short.txt')
count = 0
for line in fhand:
    if not line.startswith('From '): continue
    #print 'DEBUG:', line
    line = line.split()
    count = count + 1
    print line[1]

print "The total lines that start with \"From \" is: ", count
