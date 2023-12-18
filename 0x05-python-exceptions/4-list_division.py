#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    new_list = []
    try:
        for i in range(list_length):
            try:
                val_1 = my_list_1[i]
                val_2 = my_list_2[i]
                if not isinstance(val_1, (int, float)):
                    raise TypeError("wrong type")
                if not isinstance(val_2, (int, float)):
                    raise TypeError("wrong type")
                if val_2 == 0:
                    raise ZeroDivisionError("division by 0")
                result = val_1 / val_2
                new_list.append(result)
            except IndexError:
                print("out of range")
                new_list.append(0)
            except ZeroDivisionError:
                print("division by 0")
                new_list.append(0)
            except TypeError:
                print("wrong type")
                new_list.append(0)
    finally:
        return new_list
