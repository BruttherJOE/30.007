import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

peltier = 12
GPIO.setup(peltier, GPIO.OUT)

# CONST
start_time = time.time()
time_limiter = 10  

def control_temp()
    while elapsed_time < time_limiter:
        current_time = time.time()
        elapsed_time = current_time - start_time

        GPIO.output(peltier, GPIO.LOW)
        print("offed")
        time.sleep(3)
        print("onned")
        GPIO.output(peltier,GPIO.HIGH)
        time.sleep(2)

    print("PCR COMPLETE")
    

