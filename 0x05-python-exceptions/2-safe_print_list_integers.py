#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    count = 0
    try:
        for item in my_list:
            if count >= x:
                break
            if isinstance(item, int):
                print("{:d}".format(item), end="")
                count += 1
    except (ValueError, TypeError):
        pass
    print()
    if count < x:
        raise IndexError("list index out of range")
    return (count)
