#!/bin/python

# Chapter 6 - Strings
word = raw_input('Enter a word: ')

# Printing the word one letter at a time with index
# indefinite loop
index = 0
print 'With index < len(string)'
while index < len(word):
    print index, word[index]
    index = index + 1

# Printing the word one letter at a time
# Definite loop
print 'With for ... in ...'
for letter in word:
    print letter


# Slicing example
print 'Printing Monty Python witg slicing'
monty= 'Monty Python'
# [m,n] prints the string from position m to n, but n is not included
print 'monty[0:5]', monty[0:5]
print 'monty[6:12]', monty[6:12]
# If you want from the beggining of the string
print 'monty[:5]', monty[:5]
# If you want till the end of the string
print 'monty[6:]', monty[6:]
# The whole string
print 'monty[:]', monty[:]

# Unsing .find()
found = monty.find('ty')
print found
