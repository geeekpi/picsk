from gpiozero import MotionSensor
from picamera import PiCamera

pir = MotionSensor(4)
camera = PiCamera()

while True:
	pir.wait_for_motion()
	print("Motion detected!")

