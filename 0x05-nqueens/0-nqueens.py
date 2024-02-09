#!/usr/bin/python3
"""0. N queens"""
from sys import argv


ADD, REMOVE = 1, -1
def move_queen(queen: list[int],
               board: list[list],
               action: int) -> bool:
    """Adds or removes a queen from the board.

    Args:
        queen: a list of len 2 representing queen x and y position.
        board: 2D list representing the board.
        action: action to take, can be either ADD or REMOVE.

    Returns:
        True if action was successful, else False.
    """
    x, y = queen
    # add or remove queen if allowed.
    if action == ADD:
        if type(board[x][y]) == list or board[x][y] > 0:
            return False
        else:
            board[x][y] = queen
            print('filling', (x, y))
    elif action == REMOVE: 
        if type(board[x][y]) != list:
            return False
        else:
            board[x][y] = 0
    stack = []
    ret = True
    # iterate through the board and threaten empty cells.
    for i in range(len(board)):
        for j in range(len(board[0])):
            if (i, j) == (x, y):
                continue
            # if cell is within queen's move-set.
            if i == x or j == y or abs(x - i) == abs(y - j):
                # if cell is not empty, break.
                if action == ADD and type(board[i][j]) == list:
                    print((x, y), (i, j), ':', board[i][j])
                    ret = False
                    board[x][y] = 0
                    break
                board[i][j] += action
                stack.append((i, j))
        if not ret: break
    # if loop was broken.
    if not ret:
        # unthreaten all threatened cells.
        for i, j in stack:
            board[i][j] -= action
    # return whether action has succeded
    print(ret)
    return ret


def n_queens(n: int) -> list[list[list[int]]]:
    # make a 2D array of n * n init to 0.
    board = [[0] * n] * n
    solution_list = []
    # add new new solutions until there are none.
    while 1:
        solution = []
        while len(solution) < n:
            cell_found = False
            for x in range(n):
                for y in range(n):
                    if move_queen([x, y], board, ADD):
                        solution.append([x, y])
                        cell_found = True
                        break
                if cell_found: break
            if not cell_found:
                move_queen(solution.pop(), board, REMOVE)
        solution_list.append(solution)
        break # DEBUG
    return solution_list


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

    print(*n_queens(n), sep='\n')
