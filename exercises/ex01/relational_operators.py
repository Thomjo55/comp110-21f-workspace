"""Designed to input numbers into expression and provide feedback on whether the expression with given input is true or false."""

__author__ = "730400413"
number_one: str = input("Right-hand side: ")
number_two: str = input("Left-hand side: ")
int(number_one)
int(number_two)
print(number_one + " >= " + number_two + " is " + str(int(number_one) >= int(number_two)))
print(number_one + " < " + number_two + " is " + str(int(number_one) < int(number_two)))
print(number_one + " != " + number_two + " is " + str(int(number_one) != int(number_two)))
print(number_one + " == " + number_two + " is " + str(int(number_one) == int(number_two)))