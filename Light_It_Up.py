# Alexander
# 12/19/2017
# Light It Up

import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)

blue = 21
green = 22
red = 23
GPIO.setmode(GPIO.BCM)
GPIO.setup(blue, GPIO.OUT)
GPIO.setup(green, GPIO.OUT)
GPIO.setup(red, GPIO.OUT)
while True:
    GPIO.output(blue, GPIO.HIGH)
    time.sleep(0.35)
    GPIO.output(blue, GPIO.LOW)
    GPIO.output(green, GPIO.HIGH)
    time.sleep(0.35)
    GPIO.output(green, GPIO.LOW)
    GPIO.output(red, GPIO.HIGH)
    time.sleep(0.35)
    GPIO.output(red, GPIO.LOW)
    
    
    
    
    
    
    
    
