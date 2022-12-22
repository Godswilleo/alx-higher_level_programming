#!/usr/bin/python3
# 2-square.py by Godswill Enaohwo
"""Defines a square """


class Square:
    """Represents a square"""

    def __init__(self, size=0):
        """Initializing this square class
        Args: 
            size: represents the size of the square defined
        Raise:
            TypeError: is raised if size is not an integer
            ValueError: is less than zero
        """
        if not isinstance(size, int):
            raise TypeError('size must be an integer')
        if size < 0:
            raise ValueError('size must be >= 0')

        self.__size = size
