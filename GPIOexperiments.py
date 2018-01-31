# Setting it up
import RPi.GPIO as GPIO
import time



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

GPIO.setwarnings(False)

pwm_red.start(100)
pwm_red.stop()
pwm_green.start(100)
pwm_green.stop()
pwm_blue.start(100)
pwm_blue.stop()

# Orange
print("Orange")
pwm_red.start(85)
pwm_green.start(100)
time.sleep(2.5)

# Yellow
print("Yellow")
pwm_red.start(70)
pwm_green.start(100)
pwm_blue.start(0)
time.sleep(2.5)

# Pink
print("Pink")
pwm_red.start(45)
pwm_green.start(0)
pwm_blue.start(80)
time.sleep(2.5)

GPIO.cleanup()

