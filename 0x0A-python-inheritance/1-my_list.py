#!/usr/bin/python3
#Author: Hansel Fidel Ndemange
"""
===========================
Module with class MyList
===========================
"""


class MyList(list):
    """Class with method print_sorted"""
    pass

    def print_sorted(self):
        """Methot that sorted a list"""

        print(sorted(list(self)))

