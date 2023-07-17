# Description: Create a music player using a Raspberry Pi 4B 
# and buttons. 
# The buttons will serve as controls for playing, pausing,
# skipping tracks, and adjusting volume. 
# The project will involve connecting the buttons to 
# the Raspberry Pi's GPIO pins and programming the Pi to 
# respond to button presses with corresponding music playback actions.
# To install Pygame on a Raspberry Pi, you can follow these steps:
# * 1.	Update your system: 
# Open a terminal window on your Raspberry Pi and
# run the following commands to ensure your system is up to date:
# 
#	sudo apt-get update
#	sudo apt-get upgrade
# * 2.	Install dependencies: 
# Pygame requires several dependencies to be installed.
# Run the following command to install them:
# sudo apt-get install libsdl-dev libsdl-image1.2-dev libsdl-mixer1.2-dev libsdl-ttf2.0-dev
# 
# * 3.Install Pygame: 
#Once the dependencies are installed, you can install Pygame using
# the pip package manager. Run the following command:
#
# pip install pygame
# * 4.Verify the installation: 
# After the installation is complete, you can verify if Pygame is
# installed correctly. In the terminal, run the following command:
# python3 -m pygame.examples.aliens
#
#This command will run a Pygame example called "Aliens." 
# If a Pygame window opens and you see a game with aliens, 
#it means that Pygame is installed correctly.
#########

import pygame
import RPi.GPIO as GPIO

# Button GPIO pin numbers
PLAY_PAUSE_PIN = 18
NEXT_TRACK_PIN = 23
PREV_TRACK_PIN = 24
VOLUME_UP_PIN = 25
VOLUME_DOWN_PIN = 8

# Initialize GPIO settings
GPIO.setmode(GPIO.BCM)
GPIO.setup([PLAY_PAUSE_PIN, NEXT_TRACK_PIN, PREV_TRACK_PIN, VOLUME_UP_PIN, VOLUME_DOWN_PIN], GPIO.IN, pull_up_down=GPIO.PUD_UP)

# Initialize Pygame
pygame.mixer.init()

# Load music files (replace with your own)
music_files = ['song1.mp3', 'song2.mp3', 'song3.mp3']
current_track = 0

# Button event callbacks
def play_pause(channel):
    if pygame.mixer.music.get_busy():
        pygame.mixer.music.pause()
    else:
        pygame.mixer.music.unpause()

def next_track(channel):
    global current_track
    current_track = (current_track + 1) % len(music_files)
    pygame.mixer.music.load(music_files[current_track])
    pygame.mixer.music.play()

def prev_track(channel):
    global current_track
    current_track = (current_track - 1) % len(music_files)
    pygame.mixer.music.load(music_files[current_track])
    pygame.mixer.music.play()

def volume_up(channel):
    current_volume = pygame.mixer.music.get_volume()
    if current_volume < 1.0:
        pygame.mixer.music.set_volume(current_volume + 0.1)

def volume_down(channel):
    current_volume = pygame.mixer.music.get_volume()
    if current_volume > 0.0:
        pygame.mixer.music.set_volume(current_volume - 0.1)

# Register button event handlers
GPIO.add_event_detect(PLAY_PAUSE_PIN, GPIO.FALLING, callback=play_pause, bouncetime=200)
GPIO.add_event_detect(NEXT_TRACK_PIN, GPIO.FALLING, callback=next_track, bouncetime=200)
GPIO.add_event_detect(PREV_TRACK_PIN, GPIO.FALLING, callback=prev_track, bouncetime=200)
GPIO.add_event_detect(VOLUME_UP_PIN, GPIO.FALLING, callback=volume_up, bouncetime=200)
GPIO.add_event_detect(VOLUME_DOWN_PIN, GPIO.FALLING, callback=volume_down, bouncetime=200)

# Start playing the first track
pygame.mixer.music.load(music_files[current_track])
pygame.mixer.music.play()

try:
    # Keep the program running
    while True:
        pass
except KeyboardInterrupt:
    # Clean up GPIO and Pygame on program exit
    GPIO.cleanup()
pygame.mixer.quit()


