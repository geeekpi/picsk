# Install required Python libraries:
# - Open a terminal window and run the following commands:
#  
#   sudo apt-get update
#   sudo apt-get upgrade
#   sudo apt-get install python3-gpiozero
#
# ultrasonic_distance_demo.py
import RPi.GPIO as GPIO
import time

# Set up GPIO modes and pins
GPIO.setmode(GPIO.BCM)
TRIG = 18
ECHO = 24
GPIO.setup(TRIG, GPIO.OUT)
GPIO.setup(ECHO, GPIO.IN)

def measure_distance():
    # Trigger a pulse and wait for the echo
    GPIO.output(TRIG, True)
    time.sleep(0.00001)
    GPIO.output(TRIG, False)
    start_time = time.time()
    end_time = time.time()

    # Measure the time between sending and receiving the pulse
    while GPIO.input(ECHO) == 0:
        start_time = time.time()
    while GPIO.input(ECHO) == 1:
        end_time = time.time()

    # Calculate the distance in centimeters
    elapsed_time = end_time - start_time
    distance = (elapsed_time * 34300) / 2
    return distance

if __name__ == '__main__':
    try:
        while True:
            distance = measure_distance()
            if distance < 10:
                print("Very close!")
            elif distance < 50:
                print("Close")
            else:
                print("Far away")

            time.sleep(1)

    except KeyboardInterrupt:
        print("Measurement stopped.")
        GPIO.cleanup()

