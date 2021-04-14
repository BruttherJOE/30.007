import RPi.GPIO as GPIO
import time
import Limit_Switch_Param as LSP
import Relay_Param as RP
import stepper_param_RPI as steppy

GPIO.setmode(GPIO.BCM) # GPIO Numbers instead of board numbers

# DEFINE LIMIT SWITCH GPIO PINS
limit_switch_x = gpiozero.Button(13)
limit_switch_y = gpiozero.Button(14)
limit_switch_z = gpiozero.Button(15)

# GLOBAL VARIABLES
limit_switch_x_pressed = False

# MOVEMENT FUNCTION
def home_x():

    steppy.engageStepper()
    time.sleep(0.1)

    while global limit_switch_x_pressed = False:
        steppy.rotate(1,True,1)

        if limit_switch_x.is_pressed:
            x_pressed()

        else:
            print("Not pressed")

def x_pressed():
    limit_switch_x_pressed = True
    print("Pressed")
    steppy.rotate(180,False,0.5)
    steppy.releaseStepper()

def x_released():  #currently unused
    limit_switch_x_pressed = False
    print("Released")

# MAIN

home_x()


#functions

# limit_switch.wait_for_press()
# limit_switch.when_pressed = <do_something>
# limit_switch.when_released = <do_something>



#### TEST ####


