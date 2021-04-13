import RPi.GPIO as GPIO
import time
import gpiozero
GPIO.setmode(GPIO.BCM) # GPIO Numbers instead of board numbers

limit_switch = gpiozero.Button(13)

#functions

# limit_switch.wait_for_press()
# limit_switch.when_pressed = <do_something>
# limit_switch.when_released = <do_something>



#### TEST ####


