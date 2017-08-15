#Written by Nicholas Sullo while working at WMSI 8/17/2015
#Refer to http://abyz.co.uk/rpi/pigpio/ for more information and example code for the pigpio library

import time
import re
import pigpio
import sys

maxaltitude = 550 #Set the maximum altitude (in meters) HERE!

pi = pigpio.pi() #Setup needed to control a servo with the Pi
pi.set_mode(16, pigpio.OUTPUT) #Sets GPIO 16 as an output. GPIO 16 is not used by the Pi in the Sky Board.

pi.set_servo_pulsewidth(16, 2400) #Perform a servo check on startup
time.sleep(1) #Give the servo a chance to move
pi.set_servo_pulsewidth(16, 1000) #1000 marks the point the servo has to turn to to let go of the balloon
time.sleep(1) #Give the servo a chance to move
pi.set_servo_pulsewidth(16, 2400) #Turn back to the starting point since this is just a servo check
time.sleep(1) #Give the servo a chance to move

while 1:
	log = open('/home/pi/pits/tracker/telemetry.txt', 'r+') #This opens the log file the Pi in the sky saves to
	logout = open('/home/pi/pits/tracker/telemetrydata.txt', 'a') #This opens a file to move the telemetry data to

        telemetry = log.readlines() #Reads all the lines in the log file
        size = len(telemetry) #Determines the number of lines based on the size of the telemetry list
        last = size - 1 #The last telemetry line will be one less than the number of elements in the list since the last line of the log file is blank

        while last < 0: #The program moves faster than the log file gets filled, so if there is no more data in the log file to go through,
                telemetry = log.readlines() #keep checking the file until there is data
                size = len(telemetry)
                last = size - 1

        output = telemetry[last] 
        logout.write(output) #Write the data we just read to a new file

        log.seek(0)
        for i in telemetry:
                if i != output:
                        log.write(i)
        log.truncate() #And then get rid of the data we just read from the log file so we don't have to go through it later
        log.close() #Close the log file so it will refresh with new telemetry data from the Pi in the sky

	if output[0:10] == "$$WMSI_HAB": #Check to make sure the string is actually the telemetry data. This will have to be changed based on what you name your payload

                altpos = [m.start() for m in re.finditer(r",",output)][4] #Find the fifth instance of a comma, which will immediately preceed the altitude
	
                altpos = altpos + 1 #Move past the comma by moving forward 1 position
                altend = altpos + 5 #Determine the end of the altitude value which will always be 5 positions away
                alt = output[altpos:altend] #Using these two bounds, extract the altitude from the telemetry string
                alt = int(alt) #Turn the string altitude value into an integer

                print(alt)

                if alt >= maxaltitude: #Make sure this altitude is not larger than the predetermined cut down altitude
                        pi.set_servo_pulsewidth(16, 1000) #Turn the servo and let go of the balloon!
                        time.sleep(10)
                        pi.set_servo_pulsewidth(16, 2400) #Put the servo back down

                        break #After the servo lets go of the balloon, there is no reason for this program to continue running, so break out of all loops
                        break
                        break
        logout.close()
