#!/bin/python

var1 = raw_input('The smallest value: ')
var1= int(var1)
var2 = raw_input('The highest value: ')
var2= int(var2)

var= range(var1,var2)
print 'The length is: '
print len(var)
print 'The maximum is: '
print max(var)
print 'The minimum is: '
print min(var)
