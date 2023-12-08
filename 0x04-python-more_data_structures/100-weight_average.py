#!/usr/bin/python3
def weight_average(my_list=[]):
    if my_list is None or not my_list:
        return 0
    total = 0
    sum_weight = 0
    for val, weight in my_list:
        total = total + (val * weight)
        sum_weight = sum_weight + weight
    if sum_weight == 0:
        return 0
    avg = total / sum_weight
    return avg
