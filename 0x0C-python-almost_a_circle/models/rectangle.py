#!/usr/bin/python3
""" Module representing a rectangle """


from models.base import Base


class Rectangle(Base):
    """ Class representing a rectangle. """

    __nb_objects = 0

    def __init__(self, width, height, x=0, y=0, id=None):
        """Constructor for the Rectangle class.

        Args:
            width (int): Width of the rectangle.
            height (int): Height of the rectangle.
            x (int): x-coordinate of the rectangle.
            y (int): y-coordinate of the rectangle.
            id (int): Unique identifier for the rectangle.
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """Getter for the width attribute. """
        return self.__width

    @property
    def height(self):
        """ getter method for height """
        return self.__height

    @property
    def x(self):
        """ getter method for x """
        return self.__x

    @property
    def y(self):
        """ getter method for y """
        return self.__y

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @x.setter
    def x(self, value):
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @y.setter
    def y(self, value):
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """ returns the area of rectangle """
        return self.__height * self.__width

    def display(self):
        """Print the Rectangle instance with '#' characters."""
        for _ in range(self.y):
            print()
        for _ in range(self.height):
            print(" " * self.x + "#" * self.width)

    def to_dictionary(self):
        """Return dictionary representation of the rectangle."""
        return {
                'id': self.id,
                'width': self.width,
                'height': self.height,
                'x': self.x,
                'y': self.y
        }

    def __str__(self):
        """Overide the __str__ method."""
        return "[Rectangle] ({}) {}/{} - {}/{}".format(
                self.id, self.x, self.y, self.width, self.height
        )

    def update(self, *args, **kwargs):
        """Update attributes with arguments."""
        if args:
            attrs = ["id", "width", "height", "x", "y"]
            for attr, value in zip(attrs, args):
                setattr(self, attr, value)
        elif kwargs:
            for key, value in kwargs.items():
                setattr(self, key, value)
