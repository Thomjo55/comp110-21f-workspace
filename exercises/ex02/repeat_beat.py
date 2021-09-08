"""Repeating a beat in a loop."""

__author__ = "730400413"

counter: int = 0
beat: str = input("What beat do you want?")
repeater: int = int(input("How many times should it repeat?"))
data: str = ""
while counter < repeater:
    data = data + beat + " "
    counter = counter + 1

print(data)