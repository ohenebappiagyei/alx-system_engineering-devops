#!/usr/bin/python3
""" This module defines a class BaseGeometry with public instance methods
for area calculation and integer validation.
"""


class BaseGeometry:
    """ BaseGeometry class with public methods for area calculation and
    integer validation.

    Public methods:
    - area(self): Raises an Exception with the message 'area()
    is not implemented.'
    - integer_validator(self, name, value): Validates an integer value.

    Args:
    - name (str): The name of the value being validated.
    - value: The value to be validated.

    Raises:
    - TypeError: If the value is not an integer.
    - ValueError: If the value is less than or equal to 0.
    """
    def area(self):
        """ Raises an Exception with the message
        'area() is not implemented.'"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validates an integer value.

        Args:
            name (str): The name of the value being validated.
            value: The value to be validated.

        Raises:
            TypeError: If the value is not an integer.
            ValueError: If the value is less than or equal to 0.
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        elif value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
