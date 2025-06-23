#!/usr/bin/python3
"""Main test file for Square class."""

# Import module with explicit docstring check
module = __import__('0-square')
if module.__doc__ is None or not module.__doc__.strip():
    print("Module 0-square is not documented", end='')

Square = module.Square

my_square = Square(3)
print(type(my_square))
print(my_square.__dict__)

try:
    print(my_square.size)
except Exception as e:
    print(e)

try:
    print(my_square._size)
except Exception as e:
    print(e)
