# Alexander Nacol
# October 11, 2017
# Silly Sentence Generator 3000
# Creates silly sentences

print("*"*49)
print("* Welcome to the Silly Sentence Generator 3000! *")
print("*"*49)
      
# Getting the player's name
player_name = input("Please enter your name: ")

# + can add or join strings together
message = "Hello, " + player_name + "! Let's make a silly sentence!"
print(message)

# Gather input from the user
famous_person = input("Enter the name of a famous person: ")
adjective1 = input("Enter an adjective: ")
adjective2 = input("Enter another adjective: ")
verb = input("Enter a verb ending in -ING: ")

# Makes the silly sentence from the inputs and prints it.
sentence = ("The " + adjective1 + " " + player_name + " is " +
            verb + " the " + adjective2 + " " + famous_person + ".")
print(sentence)
