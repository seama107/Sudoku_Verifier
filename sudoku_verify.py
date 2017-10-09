#!/usr/bin/env python3
# coding: utf-8

import numpy as np
from threading import Thread

CORRECT_ROW = np.arange(1,10)

def check_puzzle(puzzle):
    # Spins off 3 threads, a row checker, a column checker, and a square checker
    # Returns a list of collisions in the following form:
    # (job_code, row, col) - row, col indexed from 0
    # EXAMPLE: the collision (2,3,4) would read
    # "Collision in Column: number X at row 4 col 5"
    # A correct puzzle returns the empty list []

    # shared_matrix_data takes the form of
    # [<original puzzle>, <results from row checker>, <results from col
    # checker>, <results from square checker>]
    shared_matrix_data = [puzzle, [],  [], []]
    threads = [ Checker_Thread(shared_matrix_data, job_code)
        for job_code in (1,2,3)]

    for t in threads:
        t.start()
    for t in threads:
        t.join()

    collisions = []
    results = shared_matrix_data[1:]
    validity_matrix = results[0]
    for i, results_matrix in enumerate(results):
        validity_matrix = np.logical_and(validity_matrix, results_matrix)
    error_matrix = np.logical_not(validity_matrix)
    return np.argwhere(error_matrix)

class Checker_Thread(Thread):
    def __init__(self, matrixes, job_code):
        Thread.__init__(self)
        self.matrixes = matrixes
        self.job_code = job_code
        if(job_code == 2):
            self.transformation = np.transpose
        elif(job_code == 3):
            self.transformation = matrix_to_subsquares
        else:
            self.transformation = identity

    def run(self):
        local_matrix = self.transformation(self.matrixes[0])
        results = check_matrix(local_matrix)
        self.matrixes[self.job_code] = self.transformation(results)

def check_row(a):
    # Takes a row, column, or square 'a' and makes sure all integers
    # 1-9 are not repeated. Returns an array of booleans where True corresponds
    # to valid number and False corresponds to a repeated number
    if(has_no_dupes(a[a!=0])):
        return np.ones(len(a), dtype=bool)

    collisions = []
    valid_slots = np.ones(len(a), dtype=bool)
    for idx in range(len(a)):
        row_data = a!=a[idx]
        row_data[idx] = True
        row_data = np.logical_or(a==0, row_data)
        valid_slots = np.logical_and(row_data, valid_slots)
    # Casting the error indexes to a boolean array of correctness per slot

    return valid_slots

def check_matrix(m):
    # Essentially runs check_row() on every row of a matrix
    output_bool_matrix = []
    for row in m:
        output_bool_matrix.append(check_row(row))
    return np.array(output_bool_matrix)

def matrix_to_subsquares(m):
    # Takes a 9x9 numpy matrix and returns a 9x9 numpy matrix where the first
    # row corresponds to the first sodoku square, the second row : second square
    # etc
    # FUN FACT. This function inverts to itself. Which is actually kinda handy
    # For this project
    subsquares = []
    for row_start in (0, 3, 6):
        for col_start in (0, 3, 6):
            subsquares.append(
                m[row_start:row_start+3,col_start:col_start+3].flatten())
    return np.array(subsquares)

def identity(matrix):
    return matrix

def has_no_dupes(a):
    return len(np.unique(a)) == len(a)
