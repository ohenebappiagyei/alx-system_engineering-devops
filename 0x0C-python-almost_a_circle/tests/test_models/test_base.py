#!/usr/bin/python3
"""Unit test for base.py"""

import unittest
from models.base import Base

class TestBase(unittest.TestCase):
    """Test cases for the Base class."""

    def test_new_instance_id(self):
        """Test creating a new instance with an automatically generated ID."""
        b1 = Base()
        b2 = Base()
        self.assertEqual(b1.id, b2.id - 1)

    def test_custom_instance_id(self):
        """Test creating a new instance with a custom ID."""
        b1 = Base(5)
        self.assertEqual(b1.id, 5)


    def test_to_json_string(self):
        """Test the to_json_string method of the Base class."""
        data = [{'id': 1, 'name': 'Alice'}, {'id': 2, 'name': 'Bob'}]
        json_str = Base.to_json_string(data)
        self.assertIsInstance(json_str, str)
        self.assertEqual(json_str, '[{"id": 1, "name": "Alice"}, {"id": 2, "name": "Bob"}]')

    def test_to_json_string_empty(self):
        """Test to_json_string with an empty list."""
        json_str = Base.to_json_string([])
        self.assertEqual(json_str, '[]')

    def test_to_json_string_none(self):
        """Test to_json_string with None."""
        json_str = Base.to_json_string(None)
        self.assertEqual(json_str, '[]')

if __name__ == "__main__":
    unittest.main()
