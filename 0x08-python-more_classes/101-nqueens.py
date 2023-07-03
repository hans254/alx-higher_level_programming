#!/usr/bin/python3
"""This module has functions for the infamous N-queens problem"""
import sys


def checkPos(board, pos):
    """Function to check if a position is valid for a queen"""
    for i in range(pos[0]):
        if board[i][pos[1]] == 1:
            return False

    for i, t in zip(range(pos[0], -1, -1), range(pos[1], -1, -1)):
        if board[i][t] == 1:
            return False

    for i, t in zip(range(pos[0], -1, -1), range(pos[1], len(board), 1)):
        if board[i][t] == 1:
            return False

    return True


def nqueens(board, row, solutions):
    """Recursive function to try board layouts"""
    if row == len(board):
        solutions.append(conv(board))

    for i in range(len(board)):
        if checkPos(board, (row, i)) is True:
            board[row][i] = 1
            nqueens(board, row + 1, solutions)
            board[row][i] = 0


def conv(sol):
    """Function to convert styles of board descriptions"""
    fun = []
    for i in range(len(sol)):
        fun.append([])
        fun[i].append(i)
        for t in range(len(sol)):
            if sol[i][t] == 1:
                fun[i].append(t)
                break
    return fun


def main():
    """Main function to check args and call recursion"""
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    try:
        number = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)
    if number < 4:
        print("N must be at least 4")
        sys.exit(1)
    board = [[0] * number for x in range(number)]
    sols = []
    nqueens(board, 0, sols)
    for x in sols:
        print(x)

if __name__ == "__main__":
    main()

