# Alexander Nacol
# 01/03/2017
# RGB Guessing Game

# Imports three things and defines functions
import RPi.GPIO as GPIO
import random
import time

number = 0


def game_over():
    '''My game over function'''
    print("You ran out of guesses! Sorry, you lose! The number was " + number + "!")

def blink_led(pin):
    '''This will blink red, green, or blue depending on the input.'''
    for i in range (5):
        GPIO.output(pin, GPIO.HIGH)
        time.sleep(0.2)
        GPIO.output(pin, GPIO.LOW)
        time.sleep(0.2)

# Sets up the GPIO pins
GPIO.setmode(GPIO.BCM)
red = 21
green = 22
blue = 23
GPIO.setup(red, GPIO.OUT)
GPIO.setup(green, GPIO.OUT)
GPIO.setup(blue, GPIO.OUT)
pwm_red = GPIO.PWM(red, 100)
pwm_green = GPIO.PWM(green, 100)
pwm_blue = GPIO.PWM(blue, 100)

# Title Screen (blinks red, green, and blue) and instructions
pwm_red.start(100)
pwm_green.start(0)
pwm_blue.start(0)
time.sleep(0.8)

pwm_red.start(0)
pwm_green.start(100)
pwm_blue.start(0)
time.sleep(0.8)

pwm_red.start(0)
pwm_green.start(0)
pwm_blue.start(100)
time.sleep(0.8)

pwm_red.stop()
pwm_green.stop()
pwm_blue.stop()


print("-"*80)
print("_"*80)
print("                           RGB GUESSING GAME                          ")
print("_"*80)
print("-"*80)

print("""
You have five guesses to guess a number between 1 and 20
Too low --> Blue blink
Too high --> Red blink
Correct --> Green blink
""")

play_again = "Y"

while play_again == "Y":
    # Get a random number that is from 1-20
    number = random.randint(1,20)
    # Start a loop
    guesses = 0
    while guesses < 5:

        # Get a guess from the user 
        guess = input("Guess a number from 1-20: ").lower()
        guesses += 1
        if guess.isdigit():
            guess = int(guess)
            # Check if guess is correct, too low, or too high
            if guess == number:
                print("You are correct! You win! Good job! Your prize is a rare bernedoodle!")
                blink_led(green)
                break
            elif guess < number:
                print ("Too low!")
                blink_led(blue)
            else:
                print("Too high!")
                blink_led(red)
        # Easter eggs!
        elif guess == "red":
            print("Red")
            pwm_red.start(100)
            time.sleep(3)
            pwm_red.stop()
            guesses -= 1
        elif guess == "blue":
            print("Blue")
            pwm_blue.start(100)
            time.sleep(3)
            pwm_blue.stop()
            guesses -= 1
        elif guess == "green":
            print("Green")
            pwm_green.start(100)
            time.sleep(3)
            pwm_green.stop()
            guesses -= 1
        elif guess == "yellow":
            print("Yellow")
            pwm_red.start(70)
            pwm_green.start(100)
            pwm_blue.start(0)
            time.sleep(3)
            pwm_red.stop()
            pwm_green.stop()
            pwm_blue.stop()
            guesses -= 1
        elif guess == "orange":
            print("Orange")
            pwm_red.start(85)
            pwm_green.start(100)
            pwm_blue.start(0)
            time.sleep(3)
            pwm_red.stop()
            pwm_green.stop()
            pwm_blue.stop()
            guesses -= 1
        elif guess == "pink":
            print("Pink")
            pwm_red.start(45)
            pwm_green.start(0)
            pwm_blue.start(80)
            time.sleep(3)
            pwm_red.stop()
            pwm_green.stop()
            pwm_blue.stop()
            guesses -= 1
        else:
            print("That is not a valid input! Try again!")
            guesses -= 1
            
    else:
        game_over()

    play_again = input("Do you play again? Enter Y for yes. ").upper()


print("Thank you for playing!")
GPIO.cleanup()

