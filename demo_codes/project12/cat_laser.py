# connection
#	Servo's VCC -> Raspberry Pi's 5V (Pin 2 or 4)
#	Servo's GND -> Raspberry Pi's GND (Pin 6, 9, 14, etc.)
#	Servo's Control -> Raspberry Pi's GPIO18 (Pin 12) 
#
#  Install the required software and libraries. 
# sudo apt-get update 
# sudo apt-get install python3-gpiozero 
# sudo apt-get install pigpio python-pigpio python3-pigpio
#
import time 
import random 
from gpiozero import Servo, OutputDevice 
import pigpio 


GPIO_SERVO = 18 
GPIO_LASER = 23

pi = pigpio.pi() 

servo = Servo(GPIO_SERVO, pin_factory=pi)
# Assumes default 50 Hz frequency, adjust if needed 

laser = OutputDevice(GPIO_LASER) 
# Function to randomly change the angle of the servo 

def random_angle():
return random.uniform(-1, 1) # Function to toggle the laser state

def toggle_laser(state): 
if state == 'ON':
    laser.on() 
else: 
    laser.off() 

try: 
toggle_laser('ON') # Turn on the laser 
while True: 
    servo.value = random_angle()
    time.sleep(random.uniform(0.5, 2))
except KeyboardInterrupt:
toggle_laser('OFF')  # Turn off the laser, when CTRL+C is pressed 

finally: pi.stop() # Stop the pigpio library


