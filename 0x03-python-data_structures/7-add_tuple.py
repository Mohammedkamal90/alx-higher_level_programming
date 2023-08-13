#!/usr/bin/python3
# 7-add_tuple.py

def add_tuple(tuple_x=(), tuple_y=()):
    """add two tuple"""
    if len(tuple_x) < 2:
        if len(tuple_x) == 0:
            tuple_x = 0, 0
        else:
            tuple_x = tuple_x[0], 0
    if len(tuple_y) < 2:
        if len(tuple_y) == 0:
            tuple_y = 0, 0
        else:
            tuple_y = tuple_y[0], 0

    return (tuple_x[0] + tuple_y[0], tuple_x[1] + tuple_y[1])
