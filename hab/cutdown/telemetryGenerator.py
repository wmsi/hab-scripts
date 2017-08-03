#!/usr/bin/python
# Mckenna Cisler - mckennacisler@gmail.com
# A script to generate realistic telemetry strings from a HAB,
# for testing nichromeCutdownController.
import time
import random

# altitudes in meters
START_ALTITUDE = 20
POP_ALTITUDE = 10000
ALTITUDE_INCREMENT = 100 # per telem packet
ALTITUDE_RANDOMNESS = 2 # meters

def generate_telemetry_string(num, alt):
    return "$$HABTWO,{},00:00:00,0.00000,0.00000,{},0,0,0,26.2,0.0,0.000*BB79\n" \
                .format(num, alt)

num = 0
delta = 1

while True:
    # the actual tracker code RE-opens the file on EACH log for appending
    # see https://github.com/PiInTheSky/pits/blob/5c14e77f671e3e21b651eaf65b83e762b94fbad8/tracker/misc.c#L41
    with open("/home/pi/pits/tracker/telemetry.txt", "at") as log:
        # add some randomness, and make sure it includes the max random value
        alt = num*ALTITUDE_INCREMENT + START_ALTITUDE + \
            int(ALTITUDE_RANDOMNESS * (random.random() + 0.25))

        telem = generate_telemetry_string(num, alt)
        log.write(telem)
        print(telem)

        # pop if we get too high
        if alt > POP_ALTITUDE:
            delta = -1
        # stop at ground
        elif alt < START_ALTITUDE:
            break

        num += delta

    # should approximate transmit time (~2.5 seconds)
    time.sleep(2.5)
