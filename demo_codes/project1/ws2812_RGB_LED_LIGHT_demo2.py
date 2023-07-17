import time

import board

import neopixel

#Initialise two light ring s variables, provide the GPIO Data Pin

# utilized and the amount of LED Nodes and brightness (0 to 1 value)

pixels1 = neopixel.NeoPixel(board.D18, 30, brightness=1)

pixels2 = neopixel.NeoPixel(board.D21, 6, brightness=1)

#Focusing on a particular light ring, use the command Fill to make it all a single color

#based on decimal code R, G, B. Number can be anything from 255 - 0. Use an RGB Colour

#Code Chart Website to quickly identify a desired fill color.

pixels1.fill((0, 255, 0))

pixels2.fill((0, 0, 255))

#Sleep for one second, and then code repeats for different color combinations. Light changes

#Could happen instead in response to certain buttons being pressed or due to threshold values

time.sleep(1.5)

pixels1.fill((200, 200, 0))

pixels2.fill((0, 200, 200))

time.sleep(1.5)

pixels1.fill((50, 70, 215))

pixels2.fill((215, 50, 70))

time.sleep(1.5)

pixels1.fill((0, 0, 0))

pixels2.fill((0, 0, 0))


