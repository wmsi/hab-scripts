#!/usr/bin/python
# Script which continually writes the time since its start
# to a file, such that, when used on a Pi running off
# battery power, the duration in the file will be the
# discharge time.
# (don't run this on startup or you'll never find your time!)
# Mckenna Cisler - mckennacisler@gmail.com

import time

WRITE_FREQ = 5 # secs
DURATION_FILE = "battery-discharge-time.txt"

start_time = time.time()

while True:
    with open(DURATION_FILE, "w+") as f:
        elapsed = time.time() - start_time # secs
        out = "%8ds (%5.2fhr) after %s" % (elapsed, \
            elapsed / 60.0, time.ctime(start_time))
        f.write(out + "\n")
        print(out)

    time.sleep(WRITE_FREQ)
