# Description: This program solves a sudoku puzzle using backtracking.


sudoku = [[0, 7, 0, 5, 8, 3, 0, 2, 0],
          [0, 5, 9, 2, 0, 0, 3, 0, 0],
          [3, 4, 0, 0, 0, 6, 5, 0, 7],
          [7, 9, 5, 0, 0, 0, 6, 3, 2],
          [0, 0, 3, 6, 9, 7, 1, 0, 0],
          [6, 8, 0, 0, 0, 2, 7, 0, 0],
          [9, 1, 4, 8, 3, 5, 0, 7, 6],
          [0, 3, 0, 7, 0, 1, 4, 9, 5],
          [5, 6, 7, 4, 2, 9, 0, 1, 3]]


def print_board(sudoku):
    for i in range(9):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - -")
        for j in range(9):
            if j % 3 == 0 and j != 0:
                print("|", end=" ")
            if j == 8:
                print(sudoku[i][j])
            else:
                print(str(sudoku[i][j]) + " ", end="")


def find_empty(sudoku):
    empty = []
    for i in range(9):
        for j in range(9):
            if sudoku[i][j] == 0:
                return (i,j)
    return None


def is_valid(sudoku, row, col, num):
    for i in range(9):
        if sudoku[row][i] == num:
            return False
    for i in range(9):
        if sudoku[i][col] == num:
            return False
    start_row = row - row % 3
    start_col = col - col % 3
    for i in range(3):
        for j in range(3):
            if sudoku[i + start_row][j + start_col] == num:
                return False
    return True

def solve(sudoku):
    find = find_empty(sudoku)
    if not find:
        return True
    else:
        row, col = find

    for i in range(1,10):
        if is_valid(sudoku,row,col,i):
            sudoku[row][col] = i

            if solve(sudoku):
                return True

            sudoku[row][col] = 0
    return False


print_board(sudoku)
empty = find_empty(sudoku)
print(empty)
solve(sudoku)
print("\n\n\n")
print_board(sudoku)