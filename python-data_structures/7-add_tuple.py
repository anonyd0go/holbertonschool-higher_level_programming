#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    new_list = [0, 0]
    for i in range(2):
        try:
            new_list[i] += tuple_a[i]
        except IndexError:
            new_list[i] += 0
        try:
            new_list[i] += tuple_b[i]
        except IndexError:
            new_list[i] += 0

    return tuple(new_list)
