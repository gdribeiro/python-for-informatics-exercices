#!/bin/python

# Exercise 6.5 chapter 6 Strings

str = 'X-DSPAM-Confidence: 0.8475'
pos = str.find(':')
str_parsed = str[(pos + 1) : ].strip()

print 'This is the string stripped: ' + str_parsed
str_parsed = float(str_parsed)
print 'This is the number in float: ', str_parsed

print 'Just printing the number with the format operator %%g: %g' % str_parsed
