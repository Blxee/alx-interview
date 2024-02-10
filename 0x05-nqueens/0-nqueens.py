#!/usr/bin/python3
"""0. N queens"""
from sys import argv


def can_move(queens, pos):
    """Determines whether a queen is safe to move to a position."""
    x1, y1 = pos
    for x2, y2 in queens[:x1]:
        if x1 == x2 or y1 == y2 or abs(x1 - x2) == abs(y1 - y2):
            return False
    return True


def n_queens(x, n, queens):
    """Prints all possiple solutions of n-queens problem."""
    if x == n:
        return print(list(queens))
    for y in range(n):
        if can_move(queens, (x, y)):
            queens[x][0], queens[x][1] = (x, y)
            n_queens(x + 1, n, queens)


if __name__ == '__main__':
    if len(argv) != 2:
        print('Usage: nqueens N')
        exit(1)

    n = argv[1]

    if not n.isdecimal():
        print('N must be a number')
        exit(1)

    n = int(n)

    if n < 4:
        print('N must be at least 4')
        exit(1)

    queens = tuple([0, 0] for _ in range(n))
    n_queens(0, n, queens)
