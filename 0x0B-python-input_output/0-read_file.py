#!/usr/bin/python3
# Hansel Fidel Ndemange

""" This module defines a function that reads a text
    file (UTF8) and prints it to stdout.
"""


def read_file(filename=""):
    """ Read a UTF8 text file and
        print it to stdout.
        param: filename - the file to open and read.
    """
    with open(filename) as f:
        text = f.read()
        for s in text:
            print(s, end='')
