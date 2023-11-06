#!/usr/bin/python3
"""
    11-square.py - Module for Square class
"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    Square class, inherits from Rectangle

    Args:
        size (int): Size of the square.

    Attributes:
        __size (int): Private instance attribute to store the size of the square.
    """

    def __init__(self, size):
        """
        Initializes a Square instance with the given size.

        Args:
            size (int): Size of the square.

        Returns:
            None
        """
        super().__init__(size, size)
        self.__size = size

    def __str__(self):
        """
        Returns a string representation of the Square.

        Returns:
            str: A string describing the square in the format [Square] <size>/<size>.
        """
        return "[" + __class__.__name__ + "] " + str(self.__size) + "/" + str(self.__size)
