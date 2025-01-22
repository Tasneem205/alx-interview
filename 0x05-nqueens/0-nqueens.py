#!/usr/bin/python3
"""Main file to solve N queens problem"""
import sys


def is_safe(board, row, col):
    """ Check if it's safe to place a queen at board[row][col]. """
    for i in range(row):
        # Check column
        if board[i] == col:
            return False
        # Check main diagonal
        if board[i] - i == col - row:
            return False
        # Check anti-diagonal
        if board[i] + i == col + row:
            return False
    return True


def solve_nqueens(row, n, board, solutions):
    """ Recursively solve the N queens problem using backtracking. """
    if row == n:
        solutions.append([[i, board[i]] for i in range(n)])
        return

    for col in range(n):
        if is_safe(board, row, col):
            board[row] = col
            solve_nqueens(row + 1, n, board, solutions)


if __name__ == "__main__":
    '''main function to take the argument'''
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    try:
        N = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)
    if N < 4:
        print("N must be at least 4")
        sys.exit(1)
    # get the solution as list
    solutions = []
    board = [-1] * N  # Represent the board as a list of column positions
    solve_nqueens(0, N, board, solutions)
    # Print all solutions
    for solution in solutions:
        print(solution)
