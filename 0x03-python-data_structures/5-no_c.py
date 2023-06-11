#!/usr/bin/python3

def no_c(my_string):
    string = ""
    for a in my_string:
        if a is not 'c' and a is not 'C':
            string += a

        return string
