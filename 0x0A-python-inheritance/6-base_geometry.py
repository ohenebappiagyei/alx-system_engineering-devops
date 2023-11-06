#!/usr/bin/python3
""" This module defines a class BaseGeometry with a public instance method
'area' that raises an Exception."""


class BaseGeometry:
    """ BaseGeometry class with an 'area' method that raises an Exception.

    Public instance method:
    - area(self): Raises an Exception with the message 'area()
    is not implemented.'
    """
    def area(self):
        """ Raises an Exception with the message
        'area() is not implemented.'"""
        raise Exception("area() is not implemented")
