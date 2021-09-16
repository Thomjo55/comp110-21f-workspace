"""Counting letters in a string."""

__author__ = "730400413"

letter: str = input("What letter do you want to search for?: ")
word: str = input("Enter a word: ")
index = 0
count: int = 0
while index < len(word):
    if letter == word[index]:
        count = count + 1
    index = index + 1
print("Count: ") + print(count)