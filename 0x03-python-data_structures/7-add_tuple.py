#!/usr/bin/python3

def add_tuple(tuple_a=(), tuple_b=()):
    tuple1_len = len(tuple_a)
    tuple2_len = len(tuple_b)

    if tuple1_len == 0:
        tuple_a = (0, 0)
    elif tuple1_len == 1:
        tuple_a = (tuple_a[0], 0)

    if tuple2_len == 0:
        tuple_b = (0, 0)
    elif tuple2_len == 1:
        tuple_b = (tuple_b[0], 0)

    a = tuple_a[0] + tuple_b[0]
    b = tuple_a[1] + tuple_b[1]

    result_tuple = (a, b)
    return result_tuple