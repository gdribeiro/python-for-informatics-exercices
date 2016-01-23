#!/bin/python

# Exercise 8.6 - Python for Informatics
# çok kolay!!!

nlist = []
while True:
    n = raw_input('Enter a number or done to finish: ')
    if n == 'done': break
    try:
        int(n)
    except:
        print 'The value was not a number!'
        exit()
    nlist.append(n)

print 'The maximum is: ', max(nlist)
print 'The minimum is: ', min(nlist)
