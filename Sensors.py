import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

# TRIG output
trig = 13

# ECHO inputs
echoC1 = 6
echoR1 = 5
echoL1 = 25
echoC2 = 24
echoR2 = 23
echoL2 = 22

# TRIG setup
GPIO.setup(trig, GPIO.OUT)

# ECHO setup
GPIO.setup(echoC1, GPIO.IN)
GPIO.setup(echoR1, GPIO.IN)
GPIO.setup(echoL1, GPIO.IN)
GPIO.setup(echoC2, GPIO.IN)
GPIO.setup(echoR2, GPIO.IN)
GPIO.setup(echoL2, GPIO.IN)

# Readings
readingC1 = 0
readingR1 = 0
readingL1 = 0
readingC2 = 0
readingR2 = 0
readingL2 = 0

def readSensors():
	readC1()
	readR1()
	readL1()
	readR2()
	readL2()
	readC2()

def readC1():
	settleSensor()
	global readingC1

	GPIO.output(trig, True)
        time.sleep(0.00001)
        GPIO.output(trig, False)

        while GPIO.input(echoC1) == 0:
                pulse_start = time.time()
        while GPIO.input(echoC1) == 1:
                pulse_end = time.time()

        pulse_duration = pulse_end - pulse_start
        readingC1 = pulse_duration * 17150
        readingC1 = round(readingC1, 2) - 0.5

def readR1():
	settleSensor()
	global readingR1

	GPIO.output(trig, True)
        time.sleep(0.00001)
        GPIO.output(trig, False)

        while GPIO.input(echoR1) == 0:
                pulse_start = time.time()
        while GPIO.input(echoR1) == 1:
                pulse_end = time.time()
        pulse_duration = pulse_end - pulse_start
        readingR1 = pulse_duration * 17150
        readingR1 = round(readingR1, 2) - 0.5

def readL1():
	settleSensor()
        global readingL1

        GPIO.output(trig, True)
        time.sleep(0.00001)
        GPIO.output(trig, False)

        while GPIO.input(echoL1) == 0:
                pulse_start = time.time()
        while GPIO.input(echoL1) == 1:
                pulse_end = time.time()
        pulse_duration = pulse_end - pulse_start
        readingL1 = pulse_duration * 17150
        readingL1 = round(readingL1, 2) - 0.5

def readC2():
	settleSensor()
        global readingC2

        GPIO.output(trig, True)
        time.sleep(0.00001)
        GPIO.output(trig, False)

        while GPIO.input(echoC2) == 0:
                pulse_start = time.time()
        while GPIO.input(echoC2) == 1:
                pulse_end = time.time()
        pulse_duration = pulse_end - pulse_start
        readingC2 = pulse_duration * 17150
        readingC2 = round(readingC2, 2) - 0.5

def readR2():
	settleSensor()
        global readingR2

        GPIO.output(trig, True)
        time.sleep(0.00001)
        GPIO.output(trig, False)

        while GPIO.input(echoR2) == 0:
                pulse_start = time.time()
        while GPIO.input(echoR2) == 1:
                pulse_end = time.time()
        pulse_duration = pulse_end - pulse_start
        readingR2 = pulse_duration * 17150
        readingR2 = round(readingR2, 2) - 0.5

def readL2():
	settleSensor()
        global readingL2

        GPIO.output(trig, True)
        time.sleep(0.00001)
        GPIO.output(trig, False)

        while GPIO.input(echoL2) == 0:
                pulse_start = time.time()
        while GPIO.input(echoL2) == 1:
                pulse_end = time.time()
        pulse_duration = pulse_end - pulse_start
        readingL2 = pulse_duration * 17150
        readingL2 = round(readingL2, 2) - 0.5

def settleSensor():
	time.sleep(0.01)

def readingC1():
	global readingC1
	return readingC1

def readingR1():
	global readingR1
	return readingR1

def readingL1():
	global readingL1
	return readingL1

def readingC2():
	global readingC2
	return readingC2

def readingR2():
	global readingR2
	return readingR2

def readingL2():
	global readingL2
	return readingL2

"""
while True:
	readSensors()

        print("C1 Distance:", readingC1, "cm")
	print("R1 Distance:", readingR1, "cm")
	print("L1 Distance:", readingL1, "cm")
	print("C2 Distance:", readingC2, "cm")
	print("R2 Distance:", readingR2, "cm")
	print("L2 Distance:", readingL2, "cm")
	print()

"""
