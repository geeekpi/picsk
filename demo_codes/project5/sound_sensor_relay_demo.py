import RPi.GPIO as GPIO

MicPin = 3
RelayPin = 4

GPIO.setwarnings(False)

GPIO.setmode(GPIO.BCM)

GPIO.setup(MicPin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

GPIO.setup(RelayPin, GPIO.OUT, initial=GPIO.LOW)

while True:
    GPIO.output(LedPin, GPIO.input(MicPin))

