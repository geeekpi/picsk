# PRINT DATA FROM A SENSOR
# The code below will display data from a DHT11 temperature 
# and humidity sensor. Follow this tutorial for instructions on 
# how to set up the DHT11 on the Raspberry Pi. 
# The DHT11 signal pin is connected to BCM pin 4 
# (physical pin 7 of the RPi).
# Temperature is displayed on line 1, 
# and humidity is displayed on line 2:
import RPi.GPIO as GPIO
import dht11
import I2C_LCD_driver


from time import *

mylcd = I2C_LCD_driver.lcd()

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.cleanup()

while True:
    instance = dht11.DHT11(pin = 4)
    result = instance.read()

# Uncomment for Fahrenheit:
# result.temperature = (result.temperature * 1.8) + 32 
    if result.is_valid():
        mylcd.lcd_display_string("Temp: %d%s C" % (result.temperature, chr(223)), 1)
        mylcd.lcd_display_string("Humidity: %d %%" % result.humidity, 2)


