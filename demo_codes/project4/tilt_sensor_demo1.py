import RPi.GPIO as GPIO
import time

# GPIO pins for tilt sensor and RGB LED
tilt_pin = 17
red_pin = 18
green_pin = 19
blue_pin = 20

# Set up GPIO mode and pins
GPIO.setmode(GPIO.BCM)
GPIO.setup(tilt_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(red_pin, GPIO.OUT)
GPIO.setup(green_pin, GPIO.OUT)
GPIO.setup(blue_pin, GPIO.OUT)

# Function to control the RGB LED based on tilt angle
def control_led(tilt_angle):
    if tilt_angle < -45:  # Strong tilt to the left
        GPIO.output(red_pin, GPIO.HIGH)
        GPIO.output(green_pin, GPIO.LOW)
        GPIO.output(blue_pin, GPIO.LOW)
    elif tilt_angle > 45:  # Strong tilt to the right
        GPIO.output(red_pin, GPIO.LOW)
        GPIO.output(green_pin, GPIO.HIGH)
        GPIO.output(blue_pin, GPIO.LOW)
    else:  # Neutral position
        GPIO.output(red_pin, GPIO.LOW)
        GPIO.output(green_pin, GPIO.LOW)
        GPIO.output(blue_pin, GPIO.HIGH)

# Main loop
try:
    while True:
        tilt_state = GPIO.input(tilt_pin)
        if tilt_state == GPIO.LOW:
            print("Tilt detected!")
            # Read the tilt angle using appropriate method or sensor library
            tilt_angle =  # Read the tilt angle here
            control_led(tilt_angle)
        time.sleep(0.1)

except KeyboardInterrupt:
GPIO.cleanup()

