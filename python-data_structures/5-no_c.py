#!/usr/bin/python3
def no_c(my_string):
    list_str = []
    for c in my_string:
        if c == 'C' or c == 'c':
            continue
        list_str.append(c)
    new_str = ''.join(list_str)
    return new_str
