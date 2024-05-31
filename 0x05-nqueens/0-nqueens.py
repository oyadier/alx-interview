#!/usr/bin/python3
"""
    The N queens puzzle involves placing N non-attacking
    queens on an N×N chessboard.
"""

import sys


class NQueens:
    """ Class for solving N Queen Problem """

    def __init__(self, n):
        self.n = n
        self.res = []

    def is_safe(self, queens, row, col):
        """ Check if it's safe to place a queen at row, col """
        for r, c in enumerate(queens):
            if c == col or abs(c - col) == abs(r - row):
                return False
        return True

    def solve(self, queens):
        """ Recursive function to solve N-Queens problem """
        row = len(queens)
        if row == self.n:
            self.res.append([[i, queens[i]] for i in range(self.n)])
            return

        for col in range(self.n):
            if self.is_safe(queens, row, col):
                self.solve(queens + [col])

    def get_solutions(self):
        """ Get all solutions for N-Queens problem """
        self.solve([])
        return self.res


# Main execution
if __name__ == "__main__":
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

    queens_solver = NQueens(N)
    solutions = queens_solver.get_solutions()

    for solution in solutions:
        print(solution)
