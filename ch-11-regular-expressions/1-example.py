#!/bin/python

# Chapter 11 - Python for Informatics examples
# Regular Expressions

# Imports the Regular Expressions Library
import re

fname = raw_input('Enter the file name: ')
if len(fname) < 1: fname = "../mbox.txt"

try:
    fhandle = open(fname, 'r')
except:
    print 'The file %s cound not be oppened.' % fname
    exit()

for line in fhandle:
    # when the line is extracted from the file it contains non-readable caracter
    # for new line and the print also includes one when executed. If this one is not
    # removed then we would have a blank line between each text line printed
    line = line.rstrip()
    # it doesn't extract the string, only return true or false if there is a match
    if re.search('^F..m', line): print line
