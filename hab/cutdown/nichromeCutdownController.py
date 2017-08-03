# Written by Nicholas Sullo while working at WMSI 8/17/2015
# Modified by Mckenna Cisler while working at WMSI 7/31/2017, to use the nichrome cutdown method
# Refer to http://abyz.co.uk/rpi/pigpio/ for more information and example code for the pigpio library

import time
import re
import RPi.GPIO as gpio
import sys

################# CONSTANTS ####################
maxaltitude = 550 # Set the maximum altitude (in meters) HERE!
callsign = "KC1EA"
nichrome_pin = 16 # TODO Sets GPIO 16 as a the nichrome output pin. GPIO 16 is not used by the Pi in the Sky Board.
nichrome_activations = 5 # number of nichrome pulses
################################################

gpio.setup(nichrome_pin, gpio.OUT)

def activate_nichrome():
    print "Activating nichrome..."
    for i in range(nichrome_activations):
         gpio.output(nichrome_pin, gpio.HIGH) # Turn on the nichrome cutdown and let go of the balloon!
         time.sleep(2) # 2 second pulse
         gpio.output(nichrome_pin, gpio.LOW) # Turn off signal (nichrome will have shut off on its own)
         time.sleep(0.1) # 100ms off time

while 1:
    # restart on any exception
    try:
    	log = open('/home/pi/pits/tracker/telemetry.txt', 'r+') # This opens the log file the Pi in the sky saves to
    	with open('/home/pi/pits/tracker/telemetrydata.txt', 'a') as logout: # This opens a file to move the telemetry data to
            telemetry = log.readlines() # Reads all the lines in the log file
            size = len(telemetry) # Determines the number of lines based on the size of the telemetry list
            last = size - 1 # The last telemetry line will be one less than the number of elements in the list since the last line of the log file is blank

            while last < 0: # The program moves faster than the log file gets filled, so if there is no more data in the log file to go through,
                telemetry = log.readlines() # keep checking the file until there is data
                size = len(telemetry)
                last = size - 1

                output = telemetry[last]
                logout.write(output) # Write the data we just read to a new file

                log.seek(0)
                for i in telemetry:
                    if i != output:
                        log.write(i)
                log.truncate() # And then get rid of the data we just read from the log file so we don't have to go through it later
                log.close() # Close the log file so it will refresh with new telemetry data from the Pi in the sky

             	if output[0:10] == "$${}}".format(callsign): # Check to make sure the string is actually the telemetry data. This will have to be changed based on what you name your payload
                     altpos = [m.start() for m in re.finditer(r",",output)][4] # Find the fifth instance of a comma, which will immediately preceed the altitude
                     altpos = altpos + 1 # Move past the comma by moving forward 1 position
                     altend = altpos + 5 # Determine the end of the altitude value which will always be 5 positions away
                     alt = output[altpos:altend] # Using these two bounds, extract the altitude from the telemetry string
                     alt = int(alt) # Turn the string altitude value into an integer

                     print(alt)

                     if alt >= maxaltitude: # Make sure this altitude is not larger than the predetermined cut down altitude
                         activate_nichrome()
                         break # After we lose the balloon, there is no reason for this program to continue running, so break out of all loops
                         break

    except SyntaxError as e:
        print "SYNTAX ERROR: {}".format(e)
    except:
        e = sys.exc_info()[0]
        print "RUNTIME ERROR: {}".format(e)
        continue
    finally:
        gpio.cleanup()
