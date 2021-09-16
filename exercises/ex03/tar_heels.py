"""An exercise in remainders and boolean logic."""

__author__ = "730400413"


numero = int(input("Enter an int: "))
if (numero % 2 == 0) and (numero % 7 == 0):
    print("TAR HEELS")
else:
    if (numero % 7 == 0):
        print("HEELS")
    else:
        if (numero % 2 == 0):
            print("TAR")
        else:
            print("CAROLINA")