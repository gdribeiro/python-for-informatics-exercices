#!/bin/python

# Import the ramdom library
# Remember that there is more ramdeom options
# The ones listed here are merelly to introduce the ramdom library
import random

print 'Pseudo Ramdoms with range()'
for i in range(5):
    x = random.random()
    print x

var1 = int(raw_input('smallest number: '))
var2 = int(raw_input('bighest number: '))

print 'Pseudo Ramdoms with rangeint()'
for i in range(5):
    x = random.randint(var1,var2)
    print x
