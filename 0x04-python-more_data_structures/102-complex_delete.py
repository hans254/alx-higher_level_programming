#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    for s in list(a_dictionary.keys()):
        if a_dictionary[s] is value:
            del a_dictionary[s]
    return a_dictionary
