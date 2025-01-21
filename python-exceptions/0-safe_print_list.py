#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    try:
        for ele in range(x):
            print("{}".format(my_list[ele]), end="")
        print()
        return ele + 1
    except IndexError:
        print()
        return ele
