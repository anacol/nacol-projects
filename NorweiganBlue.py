# Alexander Nacol
# 10/18/2017
# Norweigan Blue Guessing Game
# A guessing game

# Bringing in a random int tool
import random

# Displays the title and instructions
print("*" * 36)
print("* THE NORWEIGAN BLUE GUESSING GAME *")
print("*" * 36)

print("""
You walk into a robot store. The manager says, "Today is your lucky
day!"

He tells you that you can take home a rare (and active) Norweigan Blue Droid made
by the Galactic Empire free, if you can guess its age. You only have five
guesses, and if you get all guesses incorrect, you do not get the droid!
""")

# Makes up the parrot's age (random)
parrot_age = random.randint(1,20)

# Sets the number of guesses to 0
guesses = 0

while guesses < 5:
    # Gets a guess from the user and converts it to an integer
    guess = input("Guess the age of the droid (1-20):")
    guess = int(guess)
    guesses = guesses + 1
    # Determines if your guess is correct and tells you if it is or not
    if guess == parrot_age:
        print("""Yay! You successfully guessed the droid's age,
    and you get to keep it!""")
        break
    else:
        # TODO: Add higher or lower
        if guess < parrot_age:
            print("Too low!")
        else:
            print("Too high!")
        if guesses == 5:
            print("That was your last guess, so you lose! The parrot's age was " , parrot_age, " years old.")
print("Thank you for playing!")
        
