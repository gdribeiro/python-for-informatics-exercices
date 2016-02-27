#!/bin/python

# #!/bin/python

# Chapter 11 - Python for Informatics
# Coursera Exercise
# Regular Expressions

# Imports the Regular Expressions Library
import re

fname = "regex_sum_230554.txt"

try:
    fhandle = open(fname, 'r')
except:
    print 'The file %s cound not be oppened.' % fname
    exit()


ls = list()
for line in fhandle:
    line = line.rstrip()

    lst = re.findall('(\d+)', line)
    ls.extend(lst)

ls = map(int, ls)
s = sum(ls)
print s
