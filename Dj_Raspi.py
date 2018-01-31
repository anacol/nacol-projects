# DJ RASPI
# ALEX NACOL
# 1/16/18
# PLAYS SOUNDS WHEN A BUTTON IS PRESSED

import RPi.GPIO as GPIO
import time
import random
import os

path_ml = "/usr/share/scratch/Media/Sounds/Music Loops/"
path_v = "/usr/share/scratch/Media/Sounds/Vocals/"
path_e = "/usr/share/scratch/Media/Sounds/Effects/"

def get_MP3_sounds(sound_path):
    sound_filesound_files = os.listdir(sound_path)
    sound_filesound_files = [sound_file for sound_file in sound_filesound_files if sound_file.endswith('.mp3')]
    return sound_filesound_files

def play_random_sound(sound_path, sound_files):
    sound_file = random.choice(sound_files)
    os.system("omxplayer -o local '" + sound_path + "/" + sound_file + "' &")

sounds_ml = get_MP3_sounds(path_ml)
sounds_v = get_MP3_sounds(path_v)
sounds_e = get_MP3_sounds(path_e)

bp1 = 6
bp2 = 19

GPIO.setmode(GPIO.BCM)

GPIO.setup(bp1, GPIO.IN)
GPIO.setup(bp2, GPIO.IN)

os.system("clear")

print("""                       
DJ RASPI                        
Press button 1 for random sounds       
Press button 2 for DOY DOY DOY           
Press Ctrl + C to exit                   
    """)
while True:
    if GPIO.input(bp1) and GPIO.input(bp2):
        print("LET'S ADD EFFECTS!")
        play_random_sound(path_e, sounds_e)
        time.sleep(0.2)
    elif GPIO.input(bp1):
        print("LETS PLAY RANDOM SOUNDS")
        if random.randint(1,2) == 1:
            play_random_sound(path_ml, sounds_ml)
            time.sleep(0.2)
        else:
            play_random_sound(path_v, sounds_v)
            time.sleep(0.2)
    elif GPIO.input(bp2):
        print("DOY DOY DOY")
        os.system("omxplayer -o local '" + "/usr/share/scratch/Media/Sounds/Vocals/Doy-doy-doy.mp3' &")
        time.sleep(0.2)
    time.sleep(0.2)
