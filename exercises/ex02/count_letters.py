"""Counting letters in a string."""

__author__ = "730400413"

counter: int = 0
letter: str = input("What letter do you want to search for?")
word: str = input("Enter a word.")
while counter < len(word):
    if letter == word:
        counter = counter + 1

print(counter)