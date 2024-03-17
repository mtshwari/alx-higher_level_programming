#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    if len(matrix) == 1 and len(matrix[0]) == 0:
        print("")
    else:
        for arr in matrix:
            for m in arr:
                if m != arr[-1]:
                    print("{:d}".format(m), end=" ")
                else:
                    print("{:d}".format(m))
