# This is a python program to create a list containing squares if number is even and cube if number is odd

from random import randint

nums=[5, 6, 2, 4, 11, 5, 15, 14, 15, 4]
result=[i**2 if i % 2 == 0 else i**3 for i in nums]
print(result)
