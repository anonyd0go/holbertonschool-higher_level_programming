#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0
    weigh_sum = 0
    divisor = 0
    for score in my_list:
        weigh_sum += score[0] * score[1]
        divisor += score[1]
    return weigh_sum / divisor
