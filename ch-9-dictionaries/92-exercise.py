#!/bin/python

# Chapter 9 - Dictionaries
# Exercise 9.2
#
# Exercise 9.2 Write a program that categorizes each mail message by which day
# of the week the commit was done. To do this look for lines that start wit"From",
# then look for the third word and keep a running count of each of the days of the
# week. At the end of the program print out the contents of your dictionary (order
# does not matter).116
# Sample Line:
# From stephen.marquard@uct.ac.za Sat Jan
# Chapter 9. Dictionaries
# 5 09:14:16 2008
# Sample Execution:
# python dow.py
# Enter a file name: mbox-short.txt
# {'Fri': 20, 'Thu': 6, 'Sat': 1}

fname = raw_input('Enter the file name: ')
if len(fname) < 1 : fname = "mbox-short.txt"

try:
    fhand = open(fname, 'r')
except:
    print 'Python was unable to open the file %s' % fname
    exit()

# Reads all the file into the string 'text'
#text = fhand.read()
#print text

dic = dict()


# It could have been read directly from the file, but who cares??
# Iterates though each line and each word and add the words to the dictionary or updates the count
for line in fhand:
    if not line.startswith('From '): continue
    line = line.split()
    word = line[2]
    dic[word] = dic.get(word, 0) + 1

print dic
