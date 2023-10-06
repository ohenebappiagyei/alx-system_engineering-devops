#!/usr/bin/python3


def add_tuple(tuple_a=(), tuple_b=()):
    # Extract the first two elements from each tuple (or pad with zeros)
    a1, a2 = tuple_a[:2] + (0, 0)[:2-len(tuple_a)]
    b1, b2 = tuple_b[:2] + (0, 0)[:2-len(tuple_b)]

    # Perform addition
    sum_of_first_elements = a1 + b1
    sum_of_second_elements = a2 + b2

    # Return the result as a tuple
    return (sum_of_first_elements, sum_of_second_elements)
