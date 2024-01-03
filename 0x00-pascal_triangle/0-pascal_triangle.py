#!/usr/bin/python3
"""0. Pascal's Triangle"""


def pascal_triangle(n):
    """Creates and returns a pascal triangle of height n as 2D list.

    Args:
        n (int): the height of the triangle.

    Returns:
        list[list]: A 2d list representing triangle of height n.

    """
    if n <= 0:
        return []
    triangle = [[1]]
    for i in range(1, n):
        row = [0, *triangle[i - 1], 0]
        triangle.append([
            a + b
            for a, b in zip(row[:-1], row[1:])
        ])
    return triangle
