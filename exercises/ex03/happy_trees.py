"""Drawing forests in a loop."""

__author__ = "123456789"

# The string constant for the pine tree emoji
TREE: str = '\U0001F332'


emoji = int(input("Depth: "))
n = 0
str = ""
while n < emoji:
    str = str + TREE
    print(str)
    n = n + 1