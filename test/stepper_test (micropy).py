from machine import Pin
import time

#this is a test

onboard_led = Pin(25, Pin.OUT)

pulPin = Pin(2, Pin.OUT)
dirPin = Pin(3, Pin.OUT)
enaPin = Pin(4, Pin.OUT)

PULSE_PER_REV = 200

def step(totalPulseTime): #sec
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
    onboard_led.low()
    enaPin.high()

def engageStepper():
    onboard_led.high()
    enaPin.low()



####### TEST ########

while True:
    rotate(360, True, 0.2) #deg, isClockwise, rps
    time.sleep(1)