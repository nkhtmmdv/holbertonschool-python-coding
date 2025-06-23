#!/usr/bin/python3
"""This module defines a Square class with a private size attribute."""

class Square:
    """Represents a square defined by its size."""

    def __init__(self, size):
        """Initialize the square with the given size (no validation)."""
        self.__size = size
