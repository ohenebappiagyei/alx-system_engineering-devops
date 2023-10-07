#!/usr/bin/python3


def add_tuple(tuple_a=(), tuple_b=()):
    # If tuple_a has fewer than 2 elements, use 0 for missing values
    a = tuple_a + (0, 0)[:2 - len(tuple_a)]
    # If tuple_b has fewer than 2 elements, use 0 for missing values
    b = tuple_b + (0, 0)[:2 - len(tuple_b)]
    # Sum the corresponding elements from tuple_a and tuple_b
    result = (a[0] + b[0], a[1] + b[1])
    return (result)
