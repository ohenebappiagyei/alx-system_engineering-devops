#!/usr/bin/python3
"""
This module contains a function that adds a new attribute to an object
if it's possible. It raises a TypeError exception with the message
"can't add new attribute" if the object can't have a new attribute.
"""


def add_attribute(obj, attr, value):
    """
    Adds a new attribute to an object if it's possible.

    Args:
        obj: The object to which the attribute should be added.
        attr (str): The name of the attribute.
        value: The value of the attribute.

    Raises:
        TypeError: If the attribute already exists on the object.
    """
    if '__dict__' not in dir(obj) or hasattr(obj, attr):
        raise TypeError("can't add new attribute")
    obj.__dict__[attr] = value
