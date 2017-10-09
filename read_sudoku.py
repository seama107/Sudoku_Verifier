#!/usr/bin/env python3
# coding: utf-8

import csv
import numpy as np

VALID_CHARS=['1', '2', '3', '4', '5', '6', '7', '8', '9']
BLANK_ROW = [0]*9

def csv_to_sudoku(filename, dim=(9,9)):
    # Reading CSV files
    reader = csv.reader(open(filename, 'r'), delimiter=",")
    raw = list(reader)
    # Properly typing all characters
    ints = [list(map(input_char_to_int, row)) for row in raw]
    # Enforcing # of columns
    ints = [set_size_of_list(row, dim[0]) for row in ints]
    # Enforcing # of rows
    ints = set_size_of_list(ints, dim[1], padding=BLANK_ROW)
    return np.array(ints, dtype=int)

def input_char_to_int(c):
    if(c in VALID_CHARS):
        return int(c)
    else:
        return 0

def set_size_of_list(l, size, padding=0):
    # Returns a list of size, with extra elements described by 'padding'
    for i in range(size):
        l.append(padding)
    return l[:size]
