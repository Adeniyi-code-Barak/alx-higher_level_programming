#!/usr/bin/python3
c = ord('a')
while c <= ord('z'):
    if c != ord('q') and c != ord('e'):
        print("{:c}".format(c), end="")
    c += 1
