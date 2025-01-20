#!/usr/bin/python3
def no_c(my_string):
    list_str = list(my_string)
    if list_str:
        new_str = ""
        i = 0
        while i < len(list_str):
            if list_str[i] == 'C' or list_str[i] == 'c':
                del list_str[i]
            i += 1
        new_str = ''.join(list_str)
        return new_str
    return None
