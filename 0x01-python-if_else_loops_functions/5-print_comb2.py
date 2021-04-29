#!/usr/bin/python3
for c in range(0, 100):
    if c in range(0, 99):
        print("{}, ".format(format(c, '02d')), end='')
    else:
        print(c)
