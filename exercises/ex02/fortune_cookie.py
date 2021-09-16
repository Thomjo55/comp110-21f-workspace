"""Program that outputs one of at least four random, good fortunes."""

__author__ = "730400413"

# The randint function is imported from the random library so that
# you are able to generate integers at random.
# 
# Documentation: https://docs.python.org/3/library/random.html#random.randint
#
# For example, consider the function call expression: randint(1, 100)
# It will evaluate to an int value >= 1 and <= 100. 
from random import randint, random


x: int = randint(1, 4)
print("Your fortune cookie says...")
if x == 1:
    print("You will succeed!")
else:
    if x == 2:
        print("You will not fail!")
    else:
        if x == 3:
            print("You will have a great day!")
        else:
            if x == 4:
                print("You will not have a bad day!")


print("Now, go spread positive vibes!")