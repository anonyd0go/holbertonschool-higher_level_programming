#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        for number in row:
            if row.index(number) == len(row) - 1:
                print("{}".format(number), end="")
            else:
                print("{}".format(number), end=" ")
        print("")
