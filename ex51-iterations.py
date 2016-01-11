#!/bin/python
# It just does stupid summing up of numbers

total = 0
while True:
    num = raw_input('Type a number to be added or exit to exit: ')
    # Get the exception
    try:
        num = int(num)
    except:
        if num == 'exit':
            print 'Total= ', total
            quit()
        else:
            print 'You entered an invalid value, try again or type exit to finish.'
    # Computes the sum of the values entered
    total = total + num
    print 'Total= ', total
quit()
