import RPi.GPIO as GPIO
import time
import thread
from Sensors import *
from Motors import *

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)


# Steering memory
steeringMemory = 0 # 0 for right, left otherwise

# Constants
obstacleDistance = 15
obstacleDistance2 = 15

# LED pins
red = 27
blue = 17
amber = 4

# LED Setup
GPIO.setup(red, GPIO.OUT)
GPIO.setup(blue, GPIO.OUT)
GPIO.setup(amber, GPIO.OUT)

def rightBlocked():
	GPIO.output(red, True)
	time.sleep(0.1)
	GPIO.output(red, False)

def leftBlocked():
	GPIO.output(red, True)
        time.sleep(0.1)
        GPIO.output(red, False)

	time.sleep(0.1)

	GPIO.output(red, True)
        time.sleep(0.1)
        GPIO.output(red, False)

def programLed():
	GPIO.output(blue, True)
	time.sleep(0.1)
	GPIO.output(blue, False)

def sensorExceptionLed():
	GPIO.output(amber, True)
	time.sleep(0.1)
	GPIO.output(amber, False)

def steeringDelay():
	time.sleep(0.15)

def hardSteeringDelay():
	time.sleep(0.3)

def printReadings():
        print("- - - - - - - - - - - - -")
        print("C1 Distance:", C1, "cm")
	print("C2 Distance:", C2, "cm")
        print("R1 Distance:", R1, "cm")
        print("L1 Distance:", L1, "cm")
        print("R2 Distance:", R2, "cm")
        print("L2 Distance:", L2, "cm")
        print()

forward()

while True:
	thread.start_new_thread(programLed, ())

	try:
		readSensors()
	except UnboundLocalError:
		thread.start_new_thread(sensorExceptionLed, ())
		time.sleep(0.01)
		continue

	C1 = readingC1()
	C2 = readingC2()
	R1 = readingR1()
        L1 = readingL1()
        R2 = readingR2()
        L2 = readingL2()

	#printReadings()

	if(steeringMemory == 0):
		if(L1 <= obstacleDistance or L2 <= obstacleDistance2 or C2 <= obstacleDistance):
			thread.start_new_thread(leftBlocked, ())
			right()
			if( C2 <= obstacleDistance):
				hardSteeringDelay()
			else:
				steeringDelay()
			steeringMemory = 0
			forward()
			continue
		if(R1 <= obstacleDistance or R2 <= obstacleDistance2 or C1 <= obstacleDistance):
			thread.start_new_thread(rightBlocked, ())
                        left()
			if( C1 <= obstacleDistance):
                                hardSteeringDelay()
                        else:
                        	steeringDelay()
                        steeringMemory = 1
                        forward()
			continue
	else:
		if(R1 <= obstacleDistance or R2 <= obstacleDistance2 or C1 <= obstacleDistance):
			thread.start_new_thread(leftBlocked, ())
			left()
			if( C1 <= obstacleDistance):
                                hardSteeringDelay()
                        else:
				steeringDelay()
                        steeringMemory = 1
                        forward()
			continue
		if(L1 <= obstacleDistance or L2 <= obstacleDistance2 or C2 <= obstacleDistance):
			thread.start_new_thread(rightBlocked, ())
                        right()
			if( C2 <= obstacleDistance):
                                hardSteeringDelay()
                        else:
				steeringDelay()
                        steeringMemory = 0
                        forward()
			continue

GPIO.cleanup()
