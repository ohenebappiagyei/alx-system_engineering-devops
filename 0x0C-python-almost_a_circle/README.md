# Python - Almost a Circle

A Python project with classes and inheritance to represent and manipulate geometrical shapes.

## Table of Contents

- [Introduction](#introduction)
- [Project Structure](#project-structure)
- [How to Use](#how-to-use)
- [Running the Tests](#running-the-tests)
- [Author](#author)

## Introduction

This project focuses on creating classes and inheritance to represent and manipulate geometrical shapes in Python. The primary goal is to implement classes that model rectangles and squares while adhering to principles of object-oriented programming (OOP) and code reusability.

## Project Structure

The project is organized into the following key components:

1. **models/base.py:** The `Base` class serves as the foundation for the other classes and provides functionality for serialization and deserialization of objects to/from JSON files.

2. **models/rectangle.py:** The `Rectangle` class represents rectangles with attributes for width, height, x-coordinate, y-coordinate, and a unique identifier. It inherits from the `Base` class.

3. **models/square.py:** The `Square` class inherits from the `Rectangle` class and represents squares. It shares attributes and methods with rectangles but enforces that the width and height are always equal.

4. **tests/:** This directory contains unit tests for the project's classes. Tests are organized into separate files for `Base`, `Rectangle`, and `Square`.

## How to Use

To use the classes provided by this project, you can perform the following actions:

- Create instances of `Rectangle` and `Square` objects, specifying the required parameters (width, height, x-coordinate, y-coordinate).

- Access the attributes of the objects using the appropriate getter methods.

- Modify the attributes using the setter methods.

- Perform calculations like computing the area of rectangles and squares.

- Serialize objects to JSON representation and save them to files.

- Deserialize objects from JSON representation and load them from files.

- Display rectangles and squares using the `display` method.

- Update the attributes of objects using the `update` method.

- Generate JSON strings from a list of dictionaries or from a list of objects.

## Running the Tests

To run the unit tests for this project, you can use the `unittest` module. Here are the steps to execute the tests:

1. Navigate to the project directory.

2. Run the following command to discover and run all tests:

```bash
python3 -m unittest discover tests

Alternatively, you can run tests file by file using a command like:

```bash
python3 -m unittest tests/test_models/test_base.py

This will execute all the unit tests for the Base, Rectangle, and Square classes.


# Author
This is the response to the ALX project on "almost a circle" in the software engineering program.
