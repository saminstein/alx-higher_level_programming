#!/usr/bin/python3

def weight_average(my_list=[]):
    if my_list == 0:
        return 0

    total_score = 0
    total_weight = 0

    for elem in my_list:
        total_score += elem[0] * elem[1]
        total_weight += elem[1]
        weight_v = total_score / total_weight
    return weight_v
