#!/usr/bin/python3
"""Define a MagicClass that does exactly as the bytecode"""

import math

class MagicClass:
    """Represent a circle."""

    def __init__(self, radius=0):
        """
        Initializes a MagicClass object with the specified radius.

        Args:
            radius (float or int, optional): The radius for calculation (default is 0)

        Raises:
            TypeError: If radius is not a float or integer.
        """
        if type(radius) is not int and type(radius) is not float:
            raise TypeError('radius must be a number')
        self.__radius = radius

    def area(self):
        """
        Calculates and returns the area of a circle with specified radius

        Returns:
            floar: Thearea of the circle.
        """
        return self.__radius ** 2 * math.pi

    def circumference(self):
        """
        Calculates and returns the circumference of a circle with the specifies radius
        Returns:
            float: The circumference of the circle
        """
        return 2 * math.pi * self.__radius
