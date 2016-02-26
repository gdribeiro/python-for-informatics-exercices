#!/bin/python

# #!/bin/python

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

    # re.findall() not just find the patterns you described in the argument but also
    # returns a list with the strings that matches the pattern you searched for or
    # just the part enclosed by () in the Regular Expression
    # The pattern \S+@\S+ returns at least one non-blank caracter in each side of a @

    # relst = re.findall('\S+@\S+',line)
    # if len(relst) > 0 :
    #     print relst

    # An improved version to return only email addresses is to assure that at the beginning
    # of the addres is only letters or numbers and only letters at the end
    # For the file used here it solves the problem

    relst = re.findall('[a-zA-Z0-9]\S*@\S*[a-zA-Z]', line)
    if len(relst) > 0:
        print relst
