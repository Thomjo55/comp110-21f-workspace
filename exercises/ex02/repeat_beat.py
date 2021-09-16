"""Repeating a beat in a loop."""

__author__ = "730400413"

counter: int = 0
beat: str = input("What beat do you want?")
repeater: int = int(input("How many times should it repeat?"))
data: str = ""
if repeater <= 0:
    print("No beat...")
else:
    while counter < repeater - 1:
        data = data + beat + " "
        counter = counter + 1

print(data + beat)