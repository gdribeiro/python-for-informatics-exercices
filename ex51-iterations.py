#!/bin/python
# It just does stupid summing up of numbers

total = 0
count = 0
avg = 0
while True:
    num = raw_input('Type a number to be added or exit to exit: ')
    # Get the exception
    try:
        num = int(num)
        count = count + 1
    except:
        if num == 'exit':
            break
        else:
            print 'You entered an invalid value, try again or type exit to finish.'
    # Computes the sum of the values entered
    total = total + num
    avg = float(total) / count
    print 'Total=', total, 'Average=', avg

quit()
