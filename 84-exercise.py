#!/bin/python

# Exercise 8.4 from Python for Informatics
fhand = open('romeo.txt')

wordslist = []
for line in fhand:
    line = line.split()
    for word in line:
        if word in wordslist: continue
        wordslist.append(word)

wordslist.sort()
print wordslist
