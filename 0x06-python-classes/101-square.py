class Square:
    """Define a class Square that represents a square shape."""

    def __init__(self, size=0, position=(0, 0)):
        """
        Initialize a new square.

        Args:
            size (int): The size of the new square.
            position (tuple): The position of the new square.
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """Get the size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        """
        Set the size of the square and validate it.

        Args:
            value (int): The size of the square's sides.

        Raises:
            TypeError: If the size is not an integer.
            ValueError: If the size is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """Get the position of the square."""
        return self.__position

    @position.setter
    def position(self, value):
        """
        Set the position of the square and validate it.

        Args:
            value (tuple): The position of the square.

        Raises:
            TypeError: If the position is not a tuple of 2 positive integers.
        """
        if (
            not isinstance(value, tuple) or
            len(value) != 2 or
            not all(isinstance(x, int) and x >= 0 for x in value)
        ):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """
        Calculate and return the area of the square.

        Returns:
            int: The area of the square.
        """
        return self.__size ** 2

    def my_print(self):
        """Print the square using '#' character, respecting position."""
        if self.__size == 0:
            print()
        else:
            for _ in range(self.__position[1]):
                print()
            for _ in range(self.__size):
                print(" " * self.__position[0] + "#" * self.__size)

    def __str__(self):
        """
        Return a string representation of the square.

        Returns:
            str: The string representation of the square.
        """
        square_str = ""
        if self.__size == 0:
            return square_str
        for _ in range(self.__position[1]):
            square_str += "\n"
        for _ in range(self.__size):
            square_str += " " * self.__position[0] + "#" * self.__size + "\n"
        return square_str.rstrip()
