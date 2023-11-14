#!/usr/bin/python3
"""This is the test module for the 'Square' class"""

import unittest
from models.square import Square

class TestSquare(unittest.TestCase):
    """
    Test cases for the Rectangle class.
    """

    def test_constructor(self):
        """
        Test the constructor of the Rectangle class.
        """
        r = Square(5)
        self.assertEqual(r.id, 3)
        self.assertEqual(r.size, 5)
        self.assertEqual(r.x, 0)
        self.assertEqual(r.y, 0)

        r = Square(10, 2, 3, 4)
        self.assertEqual(r.id, 4)
        self.assertEqual(r.size, 10)
        self.assertEqual(r.x, 2)
        self.assertEqual(r.y, 3)

    def test_getter_setter(self):
        """Test the getter and setter for the size attribute."""
        r = Square(3, 1, 2)

        r.size = 4
        self.assertEqual(r.size, 4)
        self.assertEqual(r.width, 4)
        self.assertEqual(r.height, 4)

        with self.assertRaises(ValueError):
            r.size = -2


    def test_area(self):
        """Test the area method of the Square class."""
        r = Square(5)
        self.assertEqual(r.area(), 25)

        r = Square(10)
        self.assertEqual(r.area(), 100)

    def test_display(self):
        """Test the display method of the Square class."""
        r = Square(3, 1, 2)
        self.assertEqual(str(r), "[Square] (4) 1/2 - 3")

    def test_str(self):
        """Test the __str__ method of the Square class."""
        r = Square(4, 1, 2, 10)
        expected_str = "[Square] (10) 1/2 - 4"
        self.assertEqual(str(r), expected_str)

    def test_update_args(self):
        """Test the update method with *args."""
        r = Square(5)
        r.update(10, 7, 2, 8)
        expected_str = "[Square] (10) 2/8 - 7"
        self.assertEqual(str(r), expected_str)

        r.update(1, 2)
        expected_str = "[Square] (1) 2/8 - 2"
        self.assertEqual(str(r), expected_str)

    def test_update_kwargs(self):
        """Test the update method with **kwargs."""
        r = Square(5)
        r.update(x=2, y=8, id=10, size=7)
        expected_str = "[Square] (10) 2/8 - 7"
        self.assertEqual(str(r), expected_str)

        r.update(size=2, id=1)
        expected_str = "[Square] (1) 2/8 - 2"
        self.assertEqual(str(r), expected_str)

if __name__ == '__main__':
    unittest.main()

