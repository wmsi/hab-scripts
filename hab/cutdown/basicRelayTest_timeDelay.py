#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
This is a basic test script to make sure the relay is working with the selected
pin, WITH A TIME DELAY.

!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
DO NOT CONNECT THE NICHROME BEFORE STARTING THE PI.
!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
This script includes a mehtod of indicating that the script is running by
flipping the relay quickly in succession 3 times.  Once this indicator is heard,
the nichrome is safe to connect.

It was written by Asher.
Version 1.Git
"""

from nichromeControl import Nichrome
from time import sleep

timeDelay = 10 * 60

def main():
    sleep(5)
    nichrome = Nichrome()
    print(nichrome)
    # Indicate that we know the script is running:
    print "The script has been successfully initialized."
    nichrome.activate(nichromePulseCount = 3, pulseHigh = 0.005, pulseLow = 1)
    # Sleep again to indicate an obvious point in time:
    sleep(3)
    nichrome.activate(nichromePulseCount = 3, pulseHigh = 0.005, pulseLow = 1)
    # Wait before starting...
    sleep(timeDelay)
    # We only want 5 activations, so:
    nichrome.activate(5, 1, 0.5)

main()
