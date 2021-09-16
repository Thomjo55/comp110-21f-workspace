"""Finding duplicate letters in a word."""

__author__ = "730400413"

letters = str(input("Enter a word: "))
nah = bool = False

i: int = 0
while i < len(letters):
    y = letters[i]
    z = i + 1
    while z < len(letters):
        if(letters[z] == y):
            print("Found Duplicate: True")
        break
        z += 1
    i += 1

if not nah:
    print("Found Duplicate: False")