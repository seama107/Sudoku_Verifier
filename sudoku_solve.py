import numpy as np
from sudoku_verify import *

def error_matrix_to_list(error_matrix):
    return np.argwhere(error_matrix)

def solve_puzzle(puzzle, errors):
    # Implementing the backtracking algorithm
    # http://www.geeksforgeeks.org/backtracking-set-7-suduku/
    puzzle_blank = clear_errors(puzzle, errors)
    errors_to_be_fixed = np.copy(errors)
    while(len(errors_to_be_fixed) > 0):
        # Random choice of which error to try to fix
        idx = np.random.randint(len(errors_to_be_fixed))
        pair = errors_to_be_fixed[idx]
        found_num = False
        for guess in range(1,10):
            # Tries all possible entries
            puzzle_blank[pair[0],pair[1]] = guess
            if(not check_puzzle(puzzle_blank).any()):
                # If found, pop the number off the 'to be fixed' stack
                errors_to_be_fixed = np.delete(errors_to_be_fixed,idx,0)
                found_num = True
                break
        if(not found_num):
            # Back Track
            puzzle_blank = clear_errors(puzzle, errors)
            errors_to_be_fixed = np.copy(errors)
    return puzzle_blank

def clear_errors(puzzle, errors):
    puzzle_blank = np.copy(puzzle)
    for pair in errors:
        puzzle_blank[pair[0],pair[1]] = 0
    return puzzle_blank
