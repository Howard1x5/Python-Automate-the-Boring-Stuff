import time, sys

indent = 0 # How many spaces to indent

try:
    while True: # main program loop
        print(' ' * indent, end='')
        print('********')
        time.sleep(0.1) # pause for 1/10 of a second

        # dynamically determine direction without a boolean flag
        if indent == 20:
            step = -1 # start decreasing
        elif indent == 0:
            step = 1 # start increasing

        indent += step # change step dynamically

except KeyboardInterrupt:
    sys.exit()    