#!/bin/python

# Chapter 7 - Exercise 7.2

fname = raw_input('Enter the file name: ')

try:
    fh = open(fname)
except:
    print 'Error while opening the file %s' % fname
    exit()

linecount = 0
total = 0.0
for line in fh:
    if not line.startswith('X-DSPAM-Confidence:'):
        continue
    else:
        # cutting it in a ugly way
        fnumber = line[19:]
        fnumber = float(fnumber)
        total = fnumber + total
        linecount = linecount + 1

avg = total / float(linecount)
avg = round(avg, 12)

# Usint %g only prints part of the number, with limited decimal places
print 'Average spam confidence: %g' %avg

# but doing it like this is filename
print 'Average spam confidence: ', avg
