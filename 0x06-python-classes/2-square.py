#!/usr/bin/python3
"""Define a class Square."""


class Square:
    """Represent a square."""
    def __init__(self, size=0):
        """Initialize a new square with an optional size."""
        if not isinstance(size, int):
            raise TypeError("size must be an interger")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
