import RPi.GPIO as GPIO
import time

# GPIO pin numbers
MOTION_PIN = 17
LED_PIN = 18

# Initialize GPIO settings
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(MOTION_PIN, GPIO.IN)
GPIO.setup(LED_PIN, GPIO.OUT)

# Main program loop
try:
    while True:
        if GPIO.input(MOTION_PIN):
            # Motion detected
            print("Motion detected!")
            GPIO.output(LED_PIN, GPIO.HIGH)  # Turn on LED
            time.sleep(1)  # LED on duration
            GPIO.output(LED_PIN, GPIO.LOW)  # Turn off LED
        else:
            # No motion
            GPIO.output(LED_PIN, GPIO.LOW)  # Turn off LED
            time.sleep(0.1)  # Delay between readings
except KeyboardInterrupt:
    # Clean up GPIO on program exit
GPIO.cleanup()


