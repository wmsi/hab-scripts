#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Author: Asher

This function sets up the nichrome control pin as well as provides a funtion
    to cut the nichrome.

If you need to find available pins, you'll have to look at:
https://github.com/PiInTheSky/pits-hardware/blob/master/Pits-Stacking-System-GPIO-Allocations.pdf
"""

import RPi.GPIO as gpio
import time

######################### IMPORTANT VALUES
NICHROME_PIN = 1 # GPIO 0 and 1 are not used by any Pi in the Sky Boards.
NICHROME_ACTIVATIONS = 5 # number of nichrome pulses

class Nichrome:
    def __init__(self):
        gpio.setmode(gpio.BCM)
        gpio.setup(NICHROME_PIN, gpio.OUT)
        print "Initialized nichrome at {}.".format(time.strftime("%x %X %Z"))

    def activate(self, nichromePulseCount = NICHROME_ACTIVATIONS, pulseHigh = 2, pulseLow = 0.1):
        """ Activates the nichrome cutdown with a series of 2000ms/100ms on-off pulses."""
        print "Activating nichrome {} times...".format(nichromePulseCount)

        for i in range(nichromePulseCount):
            # Turn on the nichrome cutdown and let go of the balloon!
             gpio.output(NICHROME_PIN, gpio.HIGH)
             print "Sending high..."
             time.sleep(pulseHigh) # ...some pulseHigh time...

             # Turn off signal (nichrome will then shut off)
             gpio.output(NICHROME_PIN, gpio.LOW)
             print "Sending low..."
             time.sleep(pulseLow) # ...some pulseLow time...

    def disable(self):
        gpio.output(NICHROME_PIN, gpio.LOW)

    def __del__(self):
        self.disable()
        gpio.cleanup()

    def __str__(self):
        return "Nichrome object setup for pin " + str(NICHROME_PIN)
