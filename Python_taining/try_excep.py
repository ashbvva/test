#!/usr/bin/python

"""common exceptions
ValueError
ZeroDivisionError
NameError
KeyError
KeyboardInterrupt"""

ctr = 1
print("Press <ctrl>+c to exit")

try:
    while ctr:
        print(ctr)
except KeyboardInterrupt:
    print("received Keyboard Interrupt")
    import sys
    sys.exit()
except:
    print("unknown exception")
    import sys
    sys.exit()
