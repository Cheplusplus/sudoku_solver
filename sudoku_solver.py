import numpy as np
from collections import deque


class SudokuSolver:

    def __init__(self):
        self.board = np.zeros((9, 9), dtype='int8')
        self.stack = deque()

    def new_board(self, board):
        self.board[:, :] = board
        self.find_unknown()

    def get_row(self, row):
        return self.board[row, :]

    def get_column(self, column):
        return self.board[:, column]

    def get_block(self, row, column):
        if row < 3 and column < 3:
            return self.board[:3, :3]
        elif 2 < row < 6 and column < 3:
            return self.board[3:6, :3]
        elif 5 < row and column < 3:
            return self.board[6:10, :3]
        elif row < 3 and 2 < column < 6:
            return self.board[:3, 3:6]
        elif 2 < row < 6 and 2 < column < 6:
            return self.board[3:6, 3:6]
        elif 5 < row and 2 < column < 6:
            return self.board[6:10, 3:6]
        elif row < 3 and 5 < column:
            return self.board[:3, 6:10]
        elif 2 < row < 6 and 5 < column:
            return self.board[3:6, 6:10]
        else:
            return self.board[6:10, 6:10]

    def find_unknown(self):
        for row in range(0, 9):
            for column in range(0, 9):
                if self.board[row, column] == 0:
                    self.stack.append((row, column))
                    return

    def place_number(self, row, column, old_number):
        for number in range(old_number+1, 10):
            if number not in SudokuSolver.get_row(self, row) and number not in SudokuSolver.get_column(self, column)\
                    and number not in self.get_block(row, column):
                self.board[row, column] = number
                return True
        self.board[row, column] = 0
        return False

    def solve(self):
        while 0 in self.board:
            try:
                row, column = self.stack[-1]
            except IndexError:
                return False
            if self.place_number(row, column, self.board[row, column]):
                self.find_unknown()
            else:
                self.stack.pop()
        return self.board


def main():
    new_puzzle = SudokuSolver()

    # create the board
    new_puzzle.new_board(
            [[0, 0, 0, 0, 9, 0, 3, 4, 0],
             [2, 0, 7, 8, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 5, 6, 7, 0, 0],
             [8, 7, 0, 0, 0, 0, 2, 0, 0],
             [5, 0, 0, 0, 0, 0, 0, 0, 3],
             [0, 0, 9, 0, 0, 0, 0, 5, 6],
             [0, 0, 8, 9, 2, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 5, 1, 0, 9],
             [0, 2, 5, 0, 3, 0, 0, 0, 0]])

    print(new_puzzle.solve())


if __name__ == '__main__':
    main()
