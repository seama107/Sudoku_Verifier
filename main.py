#!/usr/bin/env python3
# coding: utf-8

from read_sudoku import csv_to_sudoku
from sudoku_verify import *
from sudoku_solve import *
import sys

def main(argv):
    infile = argv[0]

    puzzle = csv_to_sudoku(infile)
    errors = check_puzzle(puzzle)
    print_errors(errors, puzzle)
    if(errors.any()):
        puzzle_solved = solve_puzzle(puzzle, errors)
        print("Your solution:")
        print(puzzle)
        print("The correct solution:")
        print(puzzle_solved)

def print_errors(errors, puzzle):
    # Takes a list of 2-tuples in the form
    # (row, col) - row, col indexed from 0
    # And prints out the information in a user-friendly way
    if(errors.any()):
        for e in errors:
            row = e[0]
            col = e[1]
            repeated_number = puzzle[row,col]
            message = "Found a {} reapeated at row {}, col {}"
            print(message.format(repeated_number, row+1, col+1))
    else:
        print("The puzzle is solved correctly!")



if __name__ == '__main__':
    main(sys.argv[1:])
