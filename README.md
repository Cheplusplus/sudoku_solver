#Depth First Search Sudoku Solver

SudokuSolver() creates a new solver object.

The new_board() method takes a 9x9 array as its argument and sets the board.

The solve() method returns a solved board as a 9x9 array.

Example usage:

    # create a new instance of the solver
    new_puzzle = SudokuSolver()

    # give the solver a new puzzle 
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

    # Output the solution
    solution = new_puzzle.solve()
