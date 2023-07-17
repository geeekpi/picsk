from gpiozero import MotionSensor
from picamera import PiCamera


pir = MotionSensor(4)

while True:
	pir.wait_for_motion()
	print("Motion detected!")
