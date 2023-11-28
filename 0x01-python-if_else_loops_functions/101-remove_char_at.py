#!/usr/bin/python3
def remove_char_at(str, n):
    nw = ''
    j = 0
    for c in str:
        if j != n:
            nw += str[j]
        j += 1
    return nw
