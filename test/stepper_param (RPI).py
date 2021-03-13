import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
pulPin = GPIO.setup(2, GPIO.OUT)
dirPin = GPIO.setup(3, GPIO.OUT)
enaPin = GPIO.setup(4, GPIO.OUT)

PULSE_PER_REV = 200

def step(totalPulseTime): #in terms of seconds
    pulPin.high()
    time.sleep(totalPulseTime/2)
    pulPin.low()
    time.sleep(totalPulseTime/2)

def rotate(degrees, isClockwise, rps=1): #all values multiple of 360/PULSE_PER_REV
    pulseCount = degrees/360.0 * PULSE_PER_REV
    pulseRate = PULSE_PER_REV * rps
    rotatePulses(pulseCount, isClockwise, pulseRate)

def rotatePulses(pulseCount, isClockwise, pulseRate): #pulseRate in pulses/sec
    if isClockwise:
        dirPin.low()
    else:
        dirPin.high()
    engageStepper()
    for i in range(pulseCount):
        step(1/(pulseRate))
    releaseStepper()

    dirPin.low()

def releaseStepper():
    enaPin.high()

def engageStepper():
    enaPin.low()



####### TEST ########

while True:
    rotate(360, True, 0.2) #deg, isClockwise, rps
    time.sleep(1)