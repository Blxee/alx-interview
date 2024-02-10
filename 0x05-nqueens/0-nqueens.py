#!/usr/bin/python3
"""0. N queens"""
from sys import argv


def can_move(pos1, pos2):
    """Determines whether a queen is a target of another."""
    x1, y1 = pos1
    x2, y2 = pos2
    return x1 == x2 or y1 == y2 or abs(x1 - x2) == abs(y1 - y2)


stack = set()
board = ()


def n_queens(n, queens=set()):
    """Prints all possiple solutions of n-queens problem."""
    for pos in board:
        if pos in queens:
            continue
        for queen in queens:
            if can_move(queen, pos):
                break
        else:
            new_queens = queens | {pos}
            if len(new_queens) == n:
                solution = sum(map(hash, new_queens))
                if solution not in stack:
                    print([list(q) for q in new_queens])
                    stack.add(solution)
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

    board = tuple((x, y) for x in range(n) for y in range(n))
    n_queens(n)
