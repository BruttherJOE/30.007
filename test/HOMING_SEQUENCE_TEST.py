import RPi.GPIO as GPIO
import time
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
def home_x():

    steppy.engageStepper()
    time.sleep(0.1)

    while __name__ == "__main__":
        steppy.rotate(1,True,1,steppy.dir_x,steppy.pul_x)
        if GPIO.input(limit_switch_x) == True:    #test if theres issues here : all lim_switches maybe pressed?
            x_pressed()
            break
        else:
            print("Not pressed")

def home_y():
    
    steppy.engageStepper()
    time.sleep(0.1)

    while __name__ == "__main__":
        steppy.rotate(1,True,1,steppy.dir_y,steppy.pul_y)
        if GPIO.input(limit_switch_y) == True:
            y_pressed()
            break
        else:
            print("Not pressed")

def home_z():
    
    steppy.engageStepper()
    time.sleep(0.1)

    while __name__ == "__main__":
        steppy.rotate(1,True,1,steppy.dir_z,steppy.pul_z)
        if GPIO.input(limit_switch_z) == True:
            z_pressed()
            break
        else:
            print("Not pressed")


# MAIN
try:
    home_x()
    time.sleep(0.1)

except:
    print("error")

finally:
    steppy.releaseStepper()
    print("released")


#### TEST ####


