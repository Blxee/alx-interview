#!/usr/bin/python3
"""Island perimeter solution module."""


def island_perimeter(grid):
    """Calculates the perimeter of the island."""
    perimeter = 0
    for x in range(len(grid)):
        for y in range(len(grid[0])):
            cell = grid[x][y]
            if cell == 1:
                for i, j in [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]:
                    if not (0 <= i < len(grid)) or not (0 <= j < len(grid[0])):
                        continue
                    cell = grid[i][j]
                    if cell == 0:
                        perimeter += 1
    return perimeter
