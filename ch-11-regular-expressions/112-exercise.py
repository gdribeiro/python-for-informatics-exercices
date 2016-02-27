#!/bin/python

# #!/bin/python

# Chapter 11 - Python for Informatics
# Exercise
# Regular Expressions

# Imports the Regular Expressions Library
import re

fname = "../mbox.txt"

try:
    fhandle = open(fname, 'r')
except:
    print 'The file %s cound not be oppened.' % fname
    exit()


lavg = list()
for line in fhandle:
    line = line.rstrip()

    lex = re.findall('^N[\s\S]+: (\d+)', line)
    lavg.extend(lex)

lavg = map(int, lavg)
avg = sum(lavg) / float(len(lavg))

print 'Average= ', avg
