#!/usr/bin/python3
"""12-pascal_triangle module"""


def pascal_triangle(n):
    """returns a list of lists of integers representing
    the Pascal’s triangle of n"""

    list1 = []

    if n <= 0:
        return list1

    for i in range(n):
        row_list = []
        for j in range(i + 1):
            if j == 0 or j == i:
                row_list.append(1)
            else:
                row_list.append(list1[i - 1][j] + list1[i - 1][j - 1])

        list1.append(row_list)

    return list1
