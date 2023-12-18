#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    count = 0
    for element in range(x):
        try:
            if isinstance(my_list[element], int):
                print("{:d}".format(my_list[element]), end='')
                count += 1
        except ValueError:
            pass

    print()
    return count
