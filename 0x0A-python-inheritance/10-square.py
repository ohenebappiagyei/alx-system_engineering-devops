#!/usr/bin/python3
"""
    class Square that inherits from Rectangle
    (9-rectangle.py):

    Instantiation with size: def __init__(self, size)::
    size must be private. No getter or setter
    size must be a positive integer, validated by integer_validator
    the area() method must be implemented
"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """ Square class inherits from Rectangle """

    def __init__(self, size):
        """ initialization of Square """
        super().__init__(size, size)
        self.__size = size

    def __str__(self):
        """ returns [Square] <size>/<size> string """
        return "[" + __class__.__name__ + "] " + str(self.__size) + "/" + str(self.__size)
    