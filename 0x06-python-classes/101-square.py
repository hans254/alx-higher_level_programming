#!/usr/bin/python3
"""Module defines a Square class """


class Square:
    """ A class that defines a square by its size
    """
    def __init__(self, size=0, position=(0, 0)):
        """ Method to initialize the square object
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """ Method to returns the size value
        """
        return self.__size

    @size.setter
    def size(self, value):
        """ Method to set the size value of the square object
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """ Method that returns the position value
        """
        return self.__position

    @position.setter
    def position(self, value):
        """ Method that sets the position value of a square object
        """
        if not isinstance(value, tuple):
            raise TypeError("position must be a tuple of 2 positive integers")
        if len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if not isinstance(value[0], int):
            raise TypeError("position must be a tuple of 2 positive integers")
        if not isinstance(value[1], int):
            raise TypeError("position must be a tuple of 2 positive integers")
        if value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """ Method that returns the square are of the object
        """
        return (self.__size ** 2)

    def my_print(self):
        """ Method that prints a # square according
        to the size value
        """
        if self.size == 0:
            print()
        else:
            for a in range(self.position[1]):
                print()
            for a in range(0, self.size):
                for b in range(self.position[0]):
                    print(" ", end='')
                for c in range(self.size):
                    print("#", end='')
                print()

    def __repr__(self):
        """Prints the value of an instance of the Square class """
        newStr = ""
        if self.__size > 0:
            for a in range(self.__position[1]):
                newStr += "\n"
            for a in range(self.__size):
                for b in range(self.__position[0]):
                    newStr += " "
                for column in range(self.__size):
                    newStr += "#"
                newStr += "\n"
        else:
            newStr += "\n"
        return newStr[:-1]
