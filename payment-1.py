#!/bin/python
# Payment program
hours = raw_input('Enter the number of hours worked: ')
rate = raw_input('Enter the rate per hours: ')

# The input is of str type so it need to be trasformed to float
hours = float(hours)
rate = float(rate)

if hours <= 40:
    pay = hours * rate
else:
    pay = 40 * rate
    pay = pay + (1.5 * rate * (hours - 40))

print '\nThe result is '
print pay
print '\nThe program is over!'
