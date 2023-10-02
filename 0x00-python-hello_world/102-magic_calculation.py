#!/usr/bin/python3
def magic_calculation(a, b):
    result = 98 # LOAD_CONST 1 (98)

    # LOAD_FAST 0 (a)
    # LOAD_FAST 1 (b)
    # BINARY_POWER
    # BINARY_ADD
    result **= a
    result += b

    return (result)
