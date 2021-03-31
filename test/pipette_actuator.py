import stepper_param_RPI as steppy
import time
import RPi.GPIO as GPIO

# pipette works by pressing button down to certain height, 
# then it only draws liquid when the button is depressed.

# MAIN FUNCTION HERE
def draw_liquid(vol):
    press_pipette_button(vol)
    time.sleep(0.3)
    depress_pipette_button(vol)

# MOVEMENT FUNCTIONS HERE
def press_pipette_button(vol): #vol is in terms of degrees stepped by stepper motor
    c = 1 # constant for ppl to tune (degrees to ml) if we are not lazy
    print('pressing on pipette button...')
    steppy.engageStepper()
    time.sleep(0.1)
    steppy.rotate(c*vol,False,1)
    time.sleep(0.1)
    steppy.releaseStepper()

def depress_pipette_button(vol):
    c = 1
    print('depressing the pipette button...')
    steppy.engageStepper()
    time.sleep(0.1)
    steppy.rotate(c*vol,True,1)
    time.sleep(0.1)
    steppy.releaseStepper()


## need callibrate with limit switch? or just screw it - whatver works works

if __name__ == "__main__":
    draw_liquid(720) # just edit this number for degrees turned by stepper
