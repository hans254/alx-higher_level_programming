#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    count = 0
    length = 0

    for a in my_list:
        length += 1
    for b in range(0, x):
        try:
            print("{:d}".format(my_list[b]), end='')
            count += 1
        except (TypeError, ValueError):
            pass
    print()
    return count
