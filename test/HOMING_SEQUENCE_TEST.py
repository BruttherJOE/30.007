import RPi.GPIO as GPIO
import time
<<<<<<< HEAD
# import Limit_Switch_Param as LSP
# import Relay_Param as RP
import stepper_param_RPI as steppy

# DEFINE LIMIT SWITCH GPIO PINS
GPIO.setmode(GPIO.BCM) # GPIO Numbers instead of board numbers
limit_switch_x = 13
limit_switch_y = 14
limit_switch_z = 15

GPIO.setup(limit_switch_x, GPIO.IN, pull_up_down = GPIO.PUD_DOWN) #internal pull down
GPIO.setup(limit_switch_y, GPIO.IN, pull_up_down = GPIO.PUD_DOWN) #internal pull down
GPIO.setup(limit_switch_z, GPIO.IN, pull_up_down = GPIO.PUD_DOWN) #internal pull down

# INIT GLOBAL VARIABLES
limit_switch_x_pressed = False
limit_switch_y_pressed = False
limit_switch_z_pressed = False

# LIMIT SWITCHES FUNCTION
def x_pressed():
    limit_switch_x_pressed = True
    print("X LIMIT HIT")
    steppy.rotate(180,False,0.5,steppy.dir_x,steppy.pul_x)

def y_pressed():
    limit_switch_y_pressed = True
    print("Y LIMIT HIT")
    steppy.rotate(180,False,0.5,steppy.dir_y,steppy.dir_y)

def z_pressed():
    limit_switch_z_pressed = True
    print("Z LIMIT HIT")
    steppy.rotate(180,False,0.5,steppy.dir_z,steppy.dir_z)

# HOMING FUNCTIONS
=======
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
>>>>>>> a2be364f0c16714a776eadedf7e938bbaed5e297
def home_x():

    steppy.engageStepper()
    time.sleep(0.1)

<<<<<<< HEAD
    while __name__ == "__main__":
        steppy.rotate(1,True,1)
        if GPIO.input(limit_switch_x) == True:
            x_pressed()
            break
        else:
            print("Not pressed")

def home_y():
    pass

def home_z():
    pass


# MAIN
try:
    home_x()
    time.sleep(0.1)

except:
    print("error")

finally:
    steppy.releaseStepper()
    print("released")
=======
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

>>>>>>> a2be364f0c16714a776eadedf7e938bbaed5e297


#### TEST ####


