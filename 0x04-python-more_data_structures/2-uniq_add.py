#!/usr/bin/python3

def uniq_add(my_list=[]):
    new = list(set(my_list))
    add = 0
    for a in new:
        add += a
    return add
