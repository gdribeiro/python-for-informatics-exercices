#!/bin/python

# Exercise 6.5 chapter 6 Strings

str = raw_input('Enter you full name: ')
greet = 'Hello'
print greet + ' ' + str

# Remove spaces from the beggining and from the end of the Strings
str = str.strip()

print 'This is your name in lowercase using .lower(): ' + str.lower()
print 'This is your name in lowercase using .upper(): ' + str.upper()

sppos = str.find(' ')
print 'This is your surname: ' + str[(sppos + 1):]

index = 0
pos = 0
while pos > -1:
    index = pos
    pos = str.find(' ', index+1)
cut = str[0:(index+1)]
cutted = str.replace(cut, 'Mr. ')
print cutted

pos = str.rfind(' ')
cut = str[0:(pos+1)]
cutted = str.replace(cut, 'Mr. ')
print cutted
