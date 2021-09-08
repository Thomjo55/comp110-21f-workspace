"""Designed to input two varibales into mathematical expressions and state results."""

__author__ = "730400413"
digit_uno: str = input("Left hand side: ")
digit_dos: str = input("Right hand side: ")
int(digit_uno)
int(digit_dos)
print(digit_uno + " ** " + digit_dos + " is " + str(int(digit_uno) ** int(digit_dos)))
print(digit_uno + " / " + digit_dos + " is " + str(int(digit_uno) / int(digit_dos)))
print(digit_uno + " // " + digit_dos + " is " + str(int(digit_uno) // int(digit_dos)))
print(digit_uno + " % " + digit_dos + " is " + str(int(digit_uno) % int(digit_dos)))