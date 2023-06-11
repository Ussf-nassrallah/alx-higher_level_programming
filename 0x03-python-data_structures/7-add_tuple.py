#!/usr/bin/python3

def add_tuple(tuple_a=(), tuple_b=()):
    tuple_a += (0, 0)[:2 - len(tuple_a)]
    tuple_b += (0, 0)[:2 - len(tuple_b)]

    a = tuple_a[0] + tuple_b[0]
    b = tuple_a[1] + tuple_b[1]
    new_tuple = (a, b)

    return new_tuple
