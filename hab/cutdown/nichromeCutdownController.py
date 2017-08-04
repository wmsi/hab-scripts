#!/usr/bin/env python
"""
################################################################################
Written by Nicholas Sullo while working at WMSI 8/17/2015
Modified heavily by Mckenna Cisler (mckennacisler@gmail.com)
while working at WMSI 7/31/2017, to use the nichrome cutdown method

Refer to http://abyz.co.uk/rpi/pigpio/ for more information and
example code for the pigpio library

IMPLEMENTATION NOTE (Mckenna):
  An obvious solution to reading the logfile data is to keep the file open
  over the entire course of the program, using log.readlines() to only read
  the NEW lines. However, my fear with this solution is if the file somehow
  gets corrupted or overwritten from the beginning, in which case the program,
  sitting at a seek position 500 lines down, has to wait for 500 telem strings
  before parsing another, at which point we may be thousands of feet above
  the desired cutdown.
################################################################################
"""

import time
import re
import sys
import re
from nichromeControl import Nichrome

################################ CONSTANTS ####################################
MAX_ALTITUDE = 550 # Set the maximum altitude (in meters) HERE!
HAB_TELEM_FILE = '/home/pi/pits/tracker/telemetry.txt'
HAB_TELEM_BACKUP = '/home/pi/pits/tracker/telemetrydata.txt' # where to dump log data
###############################################################################

def loginfo(msg):
    newMsg = time.strftime("%x %X %Z | ") + msg
    print newMsg

def process_telemetry_string(telem, nichrome):
    """ Extracts and anaylzes the altitude from a raw telemetry string """
    telemFields = telem.split(",")
    try:
        # Check to make sure the string is actually the telemetry data. This will have to be changed based on what you name your payload
        if re.match("\$\$\w{1,10}", telemFields[0]) != None:
            # The 6th field in the telemetry string is the altitude
            # (Turn the string altitude value into an integer)
            alt = int(telemFields[5])

            loginfo("Altitude: {}".format(alt))

            # Make sure this altitude is not larger than the predetermined cut down altitude
            if alt >= MAX_ALTITUDE:
                nichrome.activate()
                return True

    # Continue on parsing errors
    except IndexError or ValueError:
            return False

    # not done if we're below max altitude
    return False

def main():
    loginfo("Starting controller...")
    nichrome = Nichrome()
    """ Reads telemetry lines from a logfile and transfers them to a backup file """
    # This opens the log file the Pi in the sky saves to
    with open(HAB_TELEM_FILE, 'r+') as log:
        # This opens a file to move the telemetry data to
        with open(HAB_TELEM_BACKUP, 'a') as logout:
            while True:
                # Read what lines we have
                # (from the seek position, which we enforce to be 0)
                log.seek(0)
                telemetry = log.readlines()

                # IMMEDIATELY remove the lines we just read
                # (I was inclined to delete the lines after everything had
                #  finished with the idea that if the lines below had an exception,
                #  we could re-read the data. However, I realized that it is likely
                #  that something about that data caused the error, so it's best
                #  to skip it the next time around. Additionally, clearning them
                #  below has a chance of overwriting a new line of data that had
                #  been added to the file in the interim, though this is unlikely)
                log.seek(0)
                log.truncate()

                # transfer lines from log file to logout file
                logout.writelines(telemetry)

                # process the lines
                for line in telemetry:
                    done = process_telemetry_string(line, nichrome)

                    # After we lose the balloon, there is no reason for this program to continue running, so break out of all loops
                    if done:
                        return
                        loginfo("Quit after cutdown.")

                # delay for a short bit
                time.sleep(0.25)

def create_telemetry_file():
    """ Creates the telemetry file if it isn't there """
    loginfo("Creating telem file if it doesn't exist...")
    with open(HAB_TELEM_FILE, "w"):
        pass

while True:
    # restart on any exception
    try:
        create_telemetry_file()
        main()
        break # if we finish gracefully, quit

    except SyntaxError as e:
        loginfo("SYNTAX ERROR: {}".format(e))
    except KeyboardInterrupt:
        break
    except:
        exc_type, exc_value, exc_traceback = sys.exc_info()
        loginfo("RUNTIME ERROR ({}): {}".format(exc_type, exc_value))
        continue
