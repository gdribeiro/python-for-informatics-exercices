#!/bin/python


# It just does stupid summing up of numbers

ma = None
mi = None
while True:
    num = raw_input('Type a number to be added or exit to exit: ')
    # Get the exception
    try:
        num = int(num)
    except:
        if num == 'exit':
            break
        else:
            print 'You entered an invalid value, try again or type exit to finish.'
    # Computes the sum of the values entered

    if ma is None or ma < num:
        ma = num

    if mi is None or mi > num:
        mi = num

    print 'Maximum=', ma, 'minimum=', mi

quit()
