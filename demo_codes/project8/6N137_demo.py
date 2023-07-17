import RPi.GPIO as GPIO

# Set GPIO mode and input pin
GPIO.setmode(GPIO.BCM)
input_pin = 17  # Change to your desired GPIO pin

# Configure GPIO pin as input
GPIO.setup(input_pin, GPIO.IN)

# Read input signal and print its value
try:
    while True:
        input_value = GPIO.input(input_pin)
        print("Input value:", input_value)
except KeyboardInterrupt:
    GPIO.cleanup()

