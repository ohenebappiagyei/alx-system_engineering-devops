#!/usr/bin/python3
"""
    This class defines a square and provides methods to compute its area and perform comparisons."""

class Square:
   """ 
    Attributes:
        size (float or int): The size of the square's sides.
    """

    def __init__(self, size=0):
        """
        Initializes a new square.

        Args:
            size (float or int, optional): The size of the square's sides (default is 0).

        Raises:
            TypeError: If size is not a number (float or int).
            ValueError: If size is less than 0.
        """
        if not isinstance(size, (float, int)):
            raise TypeError("size must be a number")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    @property
    def size(self):
        """
        Getter for the size attribute.

        Returns:
            float or int: The size of the square's sides.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Setter for the size attribute.

        Args:
            value (float or int): The new size for the square's sides.

        Raises:
            TypeError: If value is not a number (float or int).
            ValueError: If value is less than 0.
        """
        if not isinstance(value, (float, int)):
            raise TypeError("size must be a number")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """
        Computes the area of the square.

        Returns:
            float or int: The area of the square.
        """
        return self.__size ** 2

    def __eq__(self, other):
        """
        Checks if two squares have equal areas.

        Args:
            other (Square): The other square to compare.

        Returns:
            bool: True if areas are equal, False otherwise.
        """
        return self.area() == other.area()

    def __ne__(self, other):
        """
        Checks if two squares have different areas.

        Args:
            other (Square): The other square to compare.

        Returns:
            bool: True if areas are not equal, False otherwise.
        """
        return self.area() != other.area()

    def __lt__(self, other):
        """
        Checks if the area of the current square is less than the area of the other square.

        Args:
            other (Square): The other square to compare.

        Returns:
            bool: True if the current square's area is less, False otherwise.
        """
        return self.area() < other.area()

    def __le__(self, other):
        """
        Checks if the area of the current square is less than or equal to the area of the other square.

        Args:
            other (Square): The other square to compare.

        Returns:
            bool: True if the current square's area is less or equal, False otherwise.
        """
        return self.area() <= other.area()

    def __gt__(self, other):
        """
        Checks if the area of the current square is greater than the area of the other square.

        Args:
            other (Square): The other square to compare.

        Returns:
            bool: True if the current square's area is greater, False otherwise.
        """
        return self.area() > other.area()

    def __ge__(self, other):
        """
        Checks if the area of the current square is greater than or equal to the area of the other square.

        Args:
            other (Square): The other square to compare.

        Returns:
            bool: True if the current square's area is greater or equal, False otherwise.
        """
        return self.area() >= other.area()
