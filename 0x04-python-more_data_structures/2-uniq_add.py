#!/usr/bin/python3


def uniq_add(my_list=[]):
    uniq = set(my_list)

    sum_uniq = 0

    for item in uniq:
        sum_uniq += item

    return sum_uniq
