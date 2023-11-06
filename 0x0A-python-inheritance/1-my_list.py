#!/usr/bin/python3
"""
This module defines a class MyList that inherits from list.
"""


class MyList(list):
    """
    MyList is a subclass of list with an additional method.
    """

    def print_sorted(self):
        """
        Print the elements of the list in ascending order.
        """
        sorted_list = sorted(self)
        print(sorted_list)
