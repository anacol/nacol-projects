# PIR test
# Alex
#1\24\18

import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
PIR = 12
LED = 21
Button = 19
onoff = True


GPIO.setup(Button, GPIO.IN)
GPIO.setup(PIR, GPIO.IN)
GPIO.setup(LED, GPIO.OUT)
GPIO.output(LED, GPIO.LOW)


while True:
    if GPIO.input(Button):
        print("Button pressed.")
        if onoff == False:
            onoff = True
            print("ACTIVATING")
            for i in range(5):
                time.sleep(0.25)
                GPIO.output(LED, GPIO.HIGH)
                time.sleep(0.25)
                GPIO.output(LED, GPIO.LOW)
        else:
            onoff = False
            print("DISABLED")
    elif GPIO.input(PIR) and onoff == True:
        print("i SEEEEE you")
        GPIO.output(LED, GPIO.HIGH)
    else:
        GPIO.output(LED, GPIO.LOW)
    time.sleep(0.8)
