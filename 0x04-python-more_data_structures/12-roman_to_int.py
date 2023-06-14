#!/usr/bin/python3
def roman_to_int(roman_string):
    if roman_string and type(roman_string) is str:
        diction = dict(I=1, V=5, X=10, L=50, C=100, D=500, M=1000)
        value = 0
        for b, y in zip(roman_string, roman_string[1:]):
            if diction[b] < diction[y]:
                value -= diction[b]
            else:
                value += diction[b]
        value += diction[roman_string[-1]]
        return value
    else:
        return 0
