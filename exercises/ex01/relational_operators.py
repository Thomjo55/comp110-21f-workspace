"""Designed to input numbers into expression and provide feedback on whether the expression with given input is true or false. str(__730400413__)"""

number_one: str = input("number_one? ")
number_two: str = input("number_two? ")
print("left hand side: " + number_one)
print("right hand side: " + number_two)
int(number_one)
int(number_two)
print(number_one + " >= " + number_two + " is " + str(int(number_one) >= int(number_two)))
print(number_one + " < " + number_two + " is " + str(int(number_one) < int(number_two)))
print(number_one + " != " + number_two + " is " + str(int(number_one) != int(number_two)))
print(number_one + " == " + number_two + " is " + str(int(number_one) == int(number_two)))