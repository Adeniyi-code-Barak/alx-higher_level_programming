#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    count = 0
    for val in range(x):
        try:
            print(my_list[val], end='')
            count += 1
        except IndexError as e:
            pass

    print()
    return count
