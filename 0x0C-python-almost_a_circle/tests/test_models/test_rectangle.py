#!/usr/bin/python3
"""This is the test module for the 'Rectangle' class"""

import unittest
from models.rectangle import Rectangle

class TestRectangle(unittest.TestCase):
    """
    Test cases for the Rectangle class.
    """

    def test_constructor(self):
        """
        Test the constructor of the Rectangle class.
        """
        r = Rectangle(5, 10)
        self.assertEqual(r.width, 5)
        self.assertEqual(r.height, 10)
        self.assertEqual(r.x, 0)
        self.assertEqual(r.y, 0)
        self.assertEqual(r.id, 2)

    def test_width_setter(self):
        """
        Test the width setter method of the Rectangle class.
        """
        r = Rectangle(5, 10)
        r.width = 15
        self.assertEqual(r.width, 15)
        with self.assertRaises(ValueError):
            r.width = -10
        with self.assertRaises(TypeError):
            r.width = "invalid"

    def test_height_setter(self):
        """
        Test the height setter method of the Rectangle class.
        """
        r = Rectangle(5, 10)
        r.height = 20
        self.assertEqual(r.height, 20)
        with self.assertRaises(ValueError):
            r.height = -5
        with self.assertRaises(TypeError):
            r.height = "invalid"

    def test_x_setter(self):
        """
        Test the x setter method of the Rectangle clas.
        """
        r = Rectangle(5, 10)
        r.x = 3
        self.assertEqual(r.x, 3)
        with self.assertRaises(ValueError):
            r.x = -2
        with self.assertRaises(TypeError):
            r.x = "invalid"

    def test_y_setter(self):
        """
        Test the y setter method of the Rectangle class.
        """
        r = Rectangle(5, 10)
        r.y = 7
        self.assertEqual(r.y, 7)
        with self.assertRaises(ValueError):
            r.y = -4
        with self.assertRaises(TypeError):
            r.y = "invalid"

    def test_area(self):
        """
        Test the area method of the Rectangle class.
        """
        r = Rectangle(5, 10)
        self.assertEqual(r.area(), 50)

    def test_display(self):
        """
        Test the display method of the Rectangle class.
        """
        r = Rectangle(5, 4, 2, 3)
        with self.subTest():self.assertEqual(r.display(), None)

    def test_to_dictionary(self):
        """
        Test the to_dictionary method of the Rectangle class.
        """
        r = Rectangle(5, 10, 2, 1)
        d = r.to_dictionary()
        self.assertEqual(d, {'id': 5, 'width': 5, 'height': 10, 'x': 2, 'y': 1})

if __name__ == '__main__':
    unittest.main()
