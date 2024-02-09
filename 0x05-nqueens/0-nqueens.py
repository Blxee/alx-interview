#!/usr/bin/python3
"""0. N queens"""
from sys import argv


def can_move(pos1: list[int], pos2: list[int]) -> bool:
    """Determines whether a queen is a target of another."""
    x1, y1 = pos1
    x2, y2 = pos2
    return x1 == x2 or y1 == y2 or abs(x1 - x2) == abs(y1 - y2)


stack = []


def n_queens(n: int, queens: list[list[int]] = []) -> None:
    """Prints all possiple solutions of n-queens problem."""
    for x in range(n):
        for y in range(n):
            if [x, y] in queens:
                continue
            for qx, qy in queens:
                if can_move([qx, qy], [x, y]):
                    break
            else:
                new_queens = queens + [[x, y]]
                if len(new_queens) == n:
                    s = set([tuple(q) for q in new_queens])
                    if s not in stack:
                        print(new_queens)
                        stack.append(s)
                else:
                    n_queens(n, new_queens)


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

    n_queens(n)
