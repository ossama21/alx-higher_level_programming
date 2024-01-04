#!/usr/bin/python3
"""
nqueens backtracking program to print the coordinates of n queens
on an nxn grid such that they are all in non-attacking positions
"""


import sys


def solve_nqueens(N):
    """Solve the problem"""
    def is_safe(board, row, col):
        """Check if it's safe to place a queen at (row, col)"""
        for i in range(row):
            if board[i] == col or \
               board[i] - i == col - row or \
               board[i] + i == col + row:
                return False
        return True

    def print_solution(board):
        """Prints The solutions"""
        print('[', end="")
        for i in range(N):
            if i == N - 1:
                print("[{}, {}]".format(i, board[i]), end="")
            else:
                print("[{}, {}]".format(i, board[i]), end=", ")
        print(']')

    def backtrack(board, row):
        """The backtracking algorithm"""
        if row == N:
            """All queens are placed successfully in this configuration"""
            print_solution(board)
            return

        for col in range(N):
            if is_safe(board, row, col):
                board[row] = col
                backtrack(board, row + 1)

    """Initialize an empty board"""
    board = [-1] * N
    backtrack(board, 0)


if __name__ == "__main__":

    if len(sys.argv) != 2:
        print('Usage: nqueens N')
        sys.exit(1)
    try:
        N = int(sys.argv[1])
        if N < 4:
            print('N must be at least 4')
            sys.exit(1)
    except Exception:
        print('N must be a number')
        sys.exit(1)

    solve_nqueens(N)
