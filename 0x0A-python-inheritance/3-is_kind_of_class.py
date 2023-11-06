#!/usr/bin/python3
"""
This module defines a class that checks if an object is an instance
of a specified class or an instance of a class that inherited from the class
"""


def is_kind_of_class(obj, a_class):
    """
    Check if the given object is an instance of, or inherits from,
    the specified class.

    Args:
        obj: The object to check.
        a_class: The class to compare the object against.

    Returns:
        True if the object is an instance of, or inherits from,
        the specified class; otherwise, False.
    """
    return isinstance(obj, a_class)
