#!/usr/bin/python3
for c in range(0, 26):
    if c != 4 and c != 16:
        print("{}".format(chr(ord('a') + c)), end='')
