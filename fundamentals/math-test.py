#!/bin/python

#Test with import math
import math

# Just check it out what happens ir math is printed
#print math

print 'Enter two values to calculate the noise in decibels: '
v1 = raw_input('Enter the signal value: ')
v2 = raw_input('Enter the noise value: ')

# it has to become float or int
v1 = float(v1)
v2 = float(v2)

ratio = v1 / v2

decibels = 10 * math.log10(ratio)
print 'The signal/noise ratio in Decibels is: '
print decibels


# jsut to play with radians
radians = 0.5
height = math.sin(radians)
print height
