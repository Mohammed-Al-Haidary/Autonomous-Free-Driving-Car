import RPi.GPIO as GPIO
import time
import thread

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

# Motors
LB = 12 # Left motors spinning backwards
LF = 16 # Left motors spinning forwards
RB = 20 # Right motors spinning backwards
RF = 21 # Right motors spinning forwards

# Motor Speed Controllers
RPWM = 26
LPWM = 19

# Direction LED
green = 18

# GPIO setup
GPIO.setup(LB, GPIO.OUT)
GPIO.setup(LF, GPIO.OUT)
GPIO.setup(RB, GPIO.OUT)
GPIO.setup(RF, GPIO.OUT)
GPIO.setup(RPWM, GPIO.OUT)
GPIO.setup(LPWM, GPIO.OUT)
GPIO.setup(green, GPIO.OUT)

def rightLed():
        GPIO.output(green, True)
        time.sleep(0.1)
        GPIO.output(green, False)

def leftLed():
        GPIO.output(green, True)
        time.sleep(0.1)
        GPIO.output(green, False)

        time.sleep(0.1)

        GPIO.output(green, True)
        time.sleep(0.1)
        GPIO.output(green, False)

RS = GPIO.PWM(RPWM, 1000) # Right Speed
LS = GPIO.PWM(LPWM, 1000) # Left Speed
RS.start(100)
LS.start(100)

def forward():
	RS.ChangeDutyCycle(50)
	LS.ChangeDutyCycle(50)
	GPIO.output(LB, False)
	GPIO.output(RB, False)
	GPIO.output(LF, True)
	GPIO.output(RF, True)

def backward():
	print()
	print("GOING BACKWARD")
	print()
	RS.ChangeDutyCycle(100)
	LS.ChangeDutyCycle(100)
	GPIO.output(LF, False)
	GPIO.output(RF, False)
	GPIO.output(LB, True)
	GPIO.output(RB, True)

def right():
	thread.start_new_thread(rightLed, ())
        RS.ChangeDutyCycle(50)
        LS.ChangeDutyCycle(100)
        GPIO.output(LB, False)
        GPIO.output(RB, True)
        GPIO.output(LF, True)
        GPIO.output(RF, False)

def left():
	thread.start_new_thread(leftLed, ())
	RS.ChangeDutyCycle(100)
        LS.ChangeDutyCycle(50)
	GPIO.output(LB, True)
        GPIO.output(RB, False)
        GPIO.output(LF, False)
        GPIO.output(RF, True)

def stop():
	print()
	print("STOPPING")
	print()
	RS.ChangeDutyCycle(0)
	RS.ChangeDutyCycle(0)
	GPIO.output(LF, False)
	GPIO.output(RF, False)
	GPIO.output(LB, False)
	GPIO.output(RB, False)

"""
from Sensors import *
forward()
readC1()
print("C1:", readingC1())
time.sleep(2)

right()
time.sleep(0.5)
readC1()
print("C1:", readingC1())

left()
time.sleep(1)
readC1()
print("C1:", readingC1())

right()
time.sleep(0.5)

stop()
"""
