import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM) # GPIO Numbers instead of board numbers
 
relay_pin = 12
GPIO.setup(relay_pin, GPIO.OUT) # GPIO Assign mode

def turn_on(sleep_time):
	GPIO.output(relay_pin, GPIO.HIGH) # on
	print("onned")
	time.sleep(sleep_time)

def turn_off(sleep_time):
	GPIO.output(relay_pin, GPIO.LOW) # out
	print("offed")
	time.sleep(sleep_time)

#### TEST ####
while True:

	turn_on(0.5)
	turn_off(0.5)