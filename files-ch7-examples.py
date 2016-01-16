#!/bin/python

# Chapter 7 - Files
# Open the file handler
fhand = open('teste.txt')

# print 'File Type: '
# print type(fhand)
# print 'Filehandler information with dir(): '
# print dir(fhand)
# print 'So far so good...'
#
# count = 0
# for line in fhand:
#     count = count + 1
#     print line
# print 'Line count:', count

# Using .read() this reads the whole file into the handler
# readfromfile = fhand.read()
# print len(readfromfile)
# print readfromfile


# Just print the lines that start with # - It's a simple search
for line in fhand:
    line = line.rstrip()

    if line.startswith('#'):
        print line
