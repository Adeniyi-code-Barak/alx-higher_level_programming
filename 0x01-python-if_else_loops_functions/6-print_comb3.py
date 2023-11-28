#!/usr/bin/python3
for num in range(9):
    for digit in range(num + 1, 10):
        if num == 8:
            print("{}{}".format(num, digit))
        else:
            print("{}{}".format(num, digit), end=", ")
