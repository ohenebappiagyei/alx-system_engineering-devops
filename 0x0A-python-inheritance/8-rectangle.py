#!/usr/bin/python3
"""
This module defines the Rectangle class that inherits from BaseGeometry.
"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    Rectangle class that inherits from BaseGometry.

    Args:
        width (int): The width of the rectangle.
        height (int): The height of the rectangle.

    Attributes:
        __width (int): Private attribute for the width of the rectangle.
        __height (int): Private attribute for the height of the rectangle.

    Methods:
        __init__(self, width, height): Initializes a Rectangle
        instance with width and height.
    """

    def __init__(self, width, height):
        """
        Initialize a Rectangle instance with the specified width and height.

        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.
        """
        super().__init__()
        self.__width = 0
        self.__heigh = 0
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
