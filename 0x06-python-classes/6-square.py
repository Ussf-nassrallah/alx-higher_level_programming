#!/usr/bin/python3

""" define a Square """


class Square:
    """ represent a square """
    def __init__(self, size=0, position=(0, 0)):
        """ create a new square """
        self.size = size
        self.position = position

    def area(self):
        return self.__size * self.__size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        """ __size: private instance attribute """
        self.__size = value

    def my_print(self):
        n = self.__size
        if n == 0:
            print()
            return
        for y in range(0, self.__position[1]):
            print("")
        for index in range(0, n):
            for x in range(0, self.__position[0]):
                print(" ", end="")
            for j in range(0, n):
                print("#", end="")
            print()

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        if (not isinstance(value, tuple)
                or not all(isinstance(n, int) for n in value)
                or not all(n >= 0 for n in value)
                or len(value) != 0):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value
