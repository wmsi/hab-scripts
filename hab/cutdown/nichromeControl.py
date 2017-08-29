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
		 # See above link for what pins are taken
DEF_NICHROME_ACTIVATIONS = 10 # default number of nichrome pulses
DEF_NICHROME_HIGH_TIME = 1 # s; time during pulse that nichrome is high
DEF_NICHROME_LOW_TIME = 0.5 # s; time during pulse that nichrome is low

class Nichrome:
    def __init__(self):
        gpio.setmode(gpio.BCM)
        gpio.setup(NICHROME_PIN, gpio.OUT)
        print "Initialized nichrome at {}.".format(time.strftime("%x %X %Z"))

    def activate(self, nichromePulseCount = DEF_NICHROME_ACTIVATIONS, \
                 pulseHigh = DEF_NICHROME_HIGH_TIME, pulseLow = DEF_NICHROME_LOW_TIME):
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
             
    def indicate(self):
        """ An indicator function to signal something to the user """
        for i in range(0,3):
            self.activate(nichromePulseCount = 3, pulseHigh = 0.005, pulseLow = 0.5)
            time.sleep(2)
            
    def deactivate(self):
        gpio.output(NICHROME_PIN, gpio.LOW)

    def __del__(self):
        self.deactivate()
        gpio.cleanup()

    def __str__(self):
        return "Nichrome object setup for pin " + str(NICHROME_PIN)
