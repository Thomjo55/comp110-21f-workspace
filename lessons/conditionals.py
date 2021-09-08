"""An example of if-else statements"""

SECRET: int = 3

print("I'm thinking of a numeber between 1-5, what is it? ")
guess: int = int(input("What is your guess? "))

if guess == SECRET:
    print("You guessed correcly!!!")
    print("Good job homie g!")
else:
    print("Sorry, you guesed incorrectly :(")
    if guess > SECRET:
        print("You guessed too high!")
    else:
        ("You guessed too low!")
    
print("Game over.")