#!/usr/bin/python3
"""Main module for solution to 2d matrix rotation."""


def rotate_2d_matrix(matrix):
    """Roatates 2d matrix in-place."""
    original = [row.copy() for row in matrix]
    width, height = len(matrix[0]), len(matrix)
    for x in range(width):
        for y in range(height):
            matrix[x][y] = original[height - 1 - y][x]
