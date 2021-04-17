import RPi.GPIO as GPIO
import time

##### INIT PINS ####
# NOTICE <<< all steppers have ena pins connected >>>

# PIPETTE PINS
enaPin = 16 
dir_pip = 20
pul_pip = 21

# AXIS PINS

dir_x = 26
pul_x = 19

dir_y = 10
pul_y = 22

dir_z = 6
pul_z = 11

# GPIO CALLOUTS
GPIO.setmode(GPIO.BCM)

GPIO.setup(enaPin, GPIO.OUT)

GPIO.setup(dir_pip, GPIO.OUT)
GPIO.setup(pul_pip, GPIO.OUT)

GPIO.setup(dir_x, GPIO.OUT)
GPIO.setup(pul_x, GPIO.OUT)

GPIO.setup(dir_y, GPIO.OUT)
GPIO.setup(pul_y, GPIO.OUT)

GPIO.setup(dir_z, GPIO.OUT)
GPIO.setup(pul_z, GPIO.OUT)

# GLOBAL VARIABLES
PULSE_PER_REV = 200
VOL_PER_STEP = 2.5
EJECT_VOL = 1010

def step(totalPulseTime, PUL_PIN): #in terms of seconds
    GPIO.output(PUL_PIN,GPIO.HIGH)
    time.sleep(totalPulseTime/2)
    GPIO.output(PUL_PIN,GPIO.LOW)
    time.sleep(totalPulseTime/2)

def rotate(degrees, isClockwise, rps=1, DIR_PIN, PUL_PIN): #all values multiple of 360/PULSE_PER_REV
    pulseCount = int(degrees/360.0 * PULSE_PER_REV)
    pulseRate = PULSE_PER_REV * rps
    rotatePulses(pulseCount, isClockwise, pulseRate, DIR_PIN, PUL_PIN)

def rotatePulses(pulseCount, isClockwise, pulseRate, DIR_PIN, PUL_PIN): #pulseRate in pulses/sec
    if isClockwise:
        GPIO.output(DIR_PIN,GPIO.LOW)
    else:
        GPIO.output(DIR_PIN,GPIO.HIGH)
    engageStepper()
    for i in range(pulseCount):
        step(1/(pulseRate),PUL_PIN)
    releaseStepper()
    GPIO.output(DIR_PIN,GPIO.LOW)

def releaseStepper():
    GPIO.output(enaPin,GPIO.HIGH)

def engageStepper():
    GPIO.output(enaPin,GPIO.LOW)

def drawVolume(volume, sleepTime = 500):
    rotatePulses((int)(volume/VOL_PER_STEP), True) 
    time.sleep(sleepTime)
    rotatePulses((int)(volume/VOL_PER_STEP), False)

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