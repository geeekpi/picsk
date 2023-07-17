# Description:
# For WS2812B RGB LED Ring with 16 Nodes
# We need to plug in the 5V WS2812B Light ring 's three wires to 
# the Raspberry Pi before turning the power on. 
# *	Link the Raspberry Pi's 5V Power Input Pin with the Red Power Cabl
# *Join the white wire labeled "Ground" to the Pi's Ground pin. 
# *Join the Raspberry Pi's Green Input Pin to its GPIO 18 port. 

#With this terminal window, 
# we can search for specific programs and download them 
# from the internet. Here are the command lines you use in 
# the terminal to install everything you need. 
# Type | Y | to confirm installs if prompted.
#
#sudo pip3 install rpi_ws281x
#
#sudo pip3 install adafruit-circuitpython-neopixel
#
#sudo python3 -m pip install --force-reinstall adafruit-blinka

import time

import board

import neopixel

#Initialise, a light ring s variable, provide the GPIO Data Pin

# utilized and the amount of LED Nodes on the light ring and brightness (0 to 1 value)

pixels1 = neopixel.NeoPixel(board.D18, 55, brightness=1)

#Also, create an arbitrary count variable

x=0

pixels1.fill((0, 220, 0))

#LED Node 10 and the color Blue were selected

pixels1[10] = (0, 20, 255)

#Showing a different color

time.sleep(4)

#Below will loop until variable x has a value of 35

while x<35:

    pixels1[x] = (255, 0, 0)

    pixels1[x-5] = (255, 0, 100)

    pixels1[x-10] = (0, 0, 255)

    #Add 1 to the counter

    x=x+1

    #Add a small time pause which will translate to 'smoothly' changing color

    time.sleep(0.05)

#Below section is the same process as the above loop, just in reverse

while x>-15:

    pixels1[x] = (255, 0, 0)

    pixels1[x+5] = (255, 0, 100)

    pixels1[x+10] = (0, 255, 0)

    x=x-1

    time.sleep(0.05)

#Add a brief time delay to appreciate what has happened    

time.sleep(4)

#Complete the script by returning all the LEDs to the off

pixels1.fill((0, 0, 0))


 
