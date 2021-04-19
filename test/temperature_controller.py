import test_temperature_probe as temp
import time
import Relay_Param

start_time = time.time()
time_limiter = 10 # in terms of seconds
temperature_threshold = 40 # relay turns off/on at this threshold

# MAIN SEQ
while True:
    current_time = time.time()
    elapsed_time = current_time - start_time

    if temp.read_temp() >= temperature_threshold:
        Relay_Param.turn_off(0.2)

        if elapsed_time > time_limiter:
            print ("PCR COMPLETE")
            # continue seqeunce here by calling another def
            break

        else: 
            continue

    elif temp.read_temp() < temperature_threshold:
        Relay_Param.turn_on(0.2)



