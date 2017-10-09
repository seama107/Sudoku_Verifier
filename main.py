from read_sudoku import csv_to_sudoku
from sudoku import *
import sys

def main(argv):
    infile = argv[0]

    puzzle = csv_to_sudoku(infile)
    errors = check_puzzle(puzzle)
    print_errors(errors, puzzle)
    if(errors):
        # Continuing to try to solve the puzzle
        pass


def print_errors(error_list, puzzle):
    # Takes a list of 3-tuples in the form
    # (job_code, row, col) - row, col indexed from 0
    # And prints out the information in a user-friendly way
    chunk_names = ["row", "column", "square"]
    if(error_list):
        for e in error_list:
            chunk_name = chunk_names[e[0] - 1]
            row = e[1]
            col = e[2]
            repeated_number = puzzle[row,col]
            message = "Found a number reapeated in a {}. '{}' in row {}, col {}"
            print(message.format(chunk_name, repeated_number, row+1, col+1))
    else:
        print("The puzzle is solved correctly!")



if __name__ == '__main__':
    main(sys.argv[1:])
