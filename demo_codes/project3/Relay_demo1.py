import time
import RPi.GPIO as GPIO

relay_ch = 26

GPIO.setwarnings(False)

GPIO.setmode(GPIO.BCM)

GPIO.setup(relay_ch, GPIO.OUT)

GPIO.output(relay_ch, GPIO.LOW)

time.sleep(1)

GPIO.output(relay_ch, GPIO.HIGH)

GPIO.cleanup()

