#!/usr/bin/python3
'''Defines the Square class with getter and setter for size.'''


class Square:
    '''Represents a square with size property.'''

    def __init__(self, size=0):
        self.size = size  # Uses the setter for validation

    @property
    def size(self):
        '''Getter for the size attribute.'''
        return self.__size

    @size.setter
    def size(self, value):
        '''Setter for the size attribute with validation.'''
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        '''Returns the current square area.'''
        return self.__size ** 2
