#!/usr/bin/python3
# 9-max_integer.py


def max_integer(my_list=[]):
    """find biggest integer of the list"""
    if len(my_list) == 0:
        return (None)

    biggest = my_list[0]
    for i in range(len(my_list)):
        if my_list[i] > big:
            biggest = my_list[i]

    return (biggest)
