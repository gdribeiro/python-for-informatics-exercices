#!/bin/python

filename = raw_input('Enter the file name: ')

try:
    fhand = open(filename)
except:
    print 'Error while attempting to open the file %s' % filename

# Now reading line by line and upper casing it
for eachline in fhand:
    eachline = eachline.upper()
# use .rtri() to remove the whitespaces and \n at the end of the string
# because print puts a \n at the end of each string it prints
# So we won't have blank lines between our printed lines
    eachline = eachline.rstrip()
# Print that shit :D
    print eachline
