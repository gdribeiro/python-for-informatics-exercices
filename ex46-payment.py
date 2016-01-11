#!/bin/python

# Payment program woth functions

def computepay(h, r):
    if hours <= 40:
        pay = hours * rate
    else:
        pay = 40 * rate
        pay = pay + (1.5 * rate * (hours - 40))

    print   'The payment is: '
    print   pay
    pass

# Get the input from the user
hours   = raw_input('Enter the number of hours worked: ')
rate    = raw_input('Enter the rate per hours: ')

# Just to catch if some shit happens
try:
    # The input is of str type so it needs to be trasformed to float
    hours   = float(hours)
    rate    = float(rate)
except:
    print 'Insert only NUMBERS!!'
    quit()
