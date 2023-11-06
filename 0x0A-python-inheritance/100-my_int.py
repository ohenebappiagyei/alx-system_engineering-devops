#!/usr/bin/python3
"""
MyInt is a class that inherits from int with inverted == and != operators.
"""


class MyInt(int):
    """
    MyInt is a class that inherits from int with inverted == and != operators.
    """

    def __eq__(self, other):
        """
        Override the equality operator (==) to invert it.

        Args:
            other (int): The value to compare with.

        Returns:
            bool: True if not equal, False if equal.
        """
        return super().__ne__(other)

    def __ne__(self, other):
        """
        Override the inequality operator (!=) to invert it.

        Args:
            other (int): The value to compare with.

        Returns:
            bool: True if equal, False if not equal.
        """
        return super().__eq__(other)
