#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    is_div_list = []
    for num in my_list:
        is_div_list.append(num % 2 == 0)
    return is_div_list
