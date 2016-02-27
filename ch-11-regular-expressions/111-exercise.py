#!/bin/python

# #!/bin/python

# Chapter 11 - Python for Informatics
# Exercise
# Regular Expressions

# Imports the Regular Expressions Library
import re

reg = raw_input('Regular Expression: ')
fname = "../mbox.txt"

try:
    fhandle = open(fname, 'r')
except:
    print 'The file %s cound not be oppened.' % fname
    exit()


count = 0
for line in fhandle:
    line = line.rstrip()

    if re.search(reg, line) :
        print line
        count += 1

print 'Number of lines that matched the pattern: ', count
