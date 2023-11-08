#!/usr/bin/python3
"""
A function that returns a list of lists of integers
representing the Pascal's triangle of n
"""


def pascal_triangle(n):
    """
    Generate Pascal's triangle up to the n-th row.

    Args:
        n (int): The number of rows to generate in Pascal's triangle.

    Returns:
        list: A list of lists of integers representing Pascal's triangle

    If n is less than or equal to 0, an empty list is returned.
    """
    if n <= 0:
        return []

    triangle = [[1]]

    for i in range(1, n):
        row = [1]
        previous_row = triangle[i - 1]

        for j in range(1, i):
            row.append(previous_row[j - 1] + previous_row[j])

        row.append(1)
        triangle.append(row)

    return triangle
