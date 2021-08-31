"""Designed to input two varibales into mathematical expressions and state results. str(__730400413__)."""

digituno: str = input("digituno? ")
digitdos: str = input("digitdos? ")
print("left hand side: " + digituno)
print("right hand side: " + digitdos)
int(digituno)
int(digitdos)
print(digituno + "%" + digitdos + " is " + str(int(digituno) % int(digitdos)))
print(digituno + "**" + digitdos + " is " + str(int(digituno) ** int(digitdos)))
print(digituno + "//" + digitdos + " is " + str(int(digituno) // int(digitdos)))
print(digituno + "/" + digitdos + " is " + str(int(digituno) / int(digitdos)))