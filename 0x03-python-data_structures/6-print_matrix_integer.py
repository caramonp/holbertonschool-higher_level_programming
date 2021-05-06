#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for f in matrix:
        for idx, i in enumerate(f):
            print("{:d}".format(i), end="")
            if (idx < len(f) - 1):
                print("{}".format(" "), end="")
        print()
