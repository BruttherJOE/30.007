import RPi.GPIO as GPIO
import time

enaPin = 16
dirPin = 20
pulPin = 21

GPIO.setmode(GPIO.BCM)
GPIO.setup(enaPin, GPIO.OUT)
GPIO.setup(dirPin, GPIO.OUT)
GPIO.setup(pulPin, GPIO.OUT)

PULSE_PER_REV = 200
VOL_PER_STEP = 2.5
EJECT_VOL = 1010

def step(totalPulseTime): #in terms of seconds
    GPIO.output(pulPin,GPIO.HIGH)
    time.sleep(totalPulseTime/2)
    GPIO.output(pulPin,GPIO.LOW)
    time.sleep(totalPulseTime/2)

def rotate(degrees, isClockwise, rps=1): #all values multiple of 360/PULSE_PER_REV
    pulseCount = int(degrees/360.0 * PULSE_PER_REV)
    pulseRate = PULSE_PER_REV * rps
    rotatePulses(pulseCount, isClockwise, pulseRate)

def rotatePulses(pulseCount, isClockwise, pulseRate): #pulseRate in pulses/sec
    if isClockwise:
        GPIO.output(dirPin,GPIO.LOW)
    else:
        GPIO.output(dirPin,GPIO.HIGH)
    engageStepper()
    for i in range(pulseCount):
        step(1/(pulseRate))
    releaseStepper()

    GPIO.output(dirPin,GPIO.LOW)

def releaseStepper():
    GPIO.output(enaPin,GPIO.HIGH)

def engageStepper():
    GPIO.output(enaPin,GPIO.LOW)

def drawVolume(volume, sleepTime = 500):
    rotatePulses((int)(volume/VOL_PER_STEP), True) 
    time.sleep(sleepTime)
    rototePulses((int)(volume/VOL_PER_STEP), False)

def ejectVolume(volume = EJECT_VOL):
    drawVolume(volume)



####### TEST ########

#while True:
#    engageStepper()
#    time.sleep(2)
#
#    rotate(360, False, 1) #deg, isClockwise, rps
#    time.sleep(0.1)
#    rotate(360, True, 2)
#    time.sleep(0.1)
#    
#
#    rotate(180, False, 5)
#    time.sleep(0.1)
#    time.sleep(5)