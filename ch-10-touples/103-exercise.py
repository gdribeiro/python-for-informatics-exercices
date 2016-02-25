#!/bin/python

# This program gets the letter frequency in a file and prints a list with the letter
# in the order of most common to least common.

import string

name = raw_input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)

ddd = dict()

for line in handle:
    line = line.strip()
    line = line.translate(None, string.punctuation)
    line = line.split()
    for word in line:
        word = word.strip()
        word = word.lower()
        letter = word.split()
        for letter in word:
            if not letter <= 'z': continue
            if not letter >= 'a': continue
            ddd[letter] = ddd.get(letter, 0) + 1

lst = list()

for k,v in ddd.items():
    lst.append( (v,k) )

lst.sort(reverse=True)

for v,k in lst:
    print v,k
