import time
import RPi.GPIO as GPIO
import subprocess as sp

relay_ch = 26

GPIO.setwarnings(False)

GPIO.setmode(GPIO.BCM)

GPIO.setup(relay_ch, GPIO.OUT)

while True:
    temperature_of_cpu = sp.output('vcgencmd measure_temp').replace('temp=', '').replace('\'C', '') 
    if temperature_of_cpu >= 50:
        GPIO.output(relay_ch, GPIO.HIGH)
    else:
        GPIO.output(relay_ch, GPIO.LOW)

GPIO.cleanup()

