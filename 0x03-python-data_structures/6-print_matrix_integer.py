#!/usr/bin/python3

def print matrix_integer(matrix=[[]]):
    print('\n'.join(
        [' '.join(['{:d}'.format(idx)for idx in row])for row in matrix]
    ))
