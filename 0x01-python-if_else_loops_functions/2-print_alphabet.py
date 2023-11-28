#!/usr/bin/python3
c = ord('a')
while c <= ord('z'):
    print("{:c}".format(c), end="")
    c += 1
