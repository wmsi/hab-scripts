Setting up WMSI Nichrome Cutdown Scripts

[Physical Nichrome Design](https://docs.google.com/document/d/1if0S766RU5wZ8iE2Y9442clqn32jEeF_cgAFM9OfUlE/edit#heading=h.4vyrf2d91247)

[GitHub folder with these scripts](https://github.com/wmsi/hab-scripts/tree/master/hab/cutdown)

# Overview

**As of fall, 2017, Pin: Physical 28, BCM 1, Name ID_SC**

There are several nichrome-related scripts (found [here](https://github.com/wmsi/hab-scripts/tree/master/hab/cutdown)), but the important ones are: 

**[nichromeCutdownController.p**y](https://github.com/wmsi/hab-scripts/blob/master/hab/cutdown/nichromeCutdownController.py) - responsible for the altitude-based cutdown. Reads telemetry strings from the Pi In The Sky logs, dumps those strings to another log file, and extracts the altitude from the strings and checks it against a preset cutdown altitude. 

**[basicRelayTest_timeDelay.p**y](https://github.com/wmsi/hab-scripts/blob/master/hab/cutdown/basicRelayTest_timeDelay.py) - a testing script that activates the relay after a certain amount of time.

**[nichromeControl.p**y](https://github.com/wmsi/hab-scripts/blob/master/hab/cutdown/nichromeControl.py) - responsible for the specifics of activating the nichrome, i.e. the timing and quantity of pulses, etc.

	**[basicRelayTest.p**y](https://github.com/wmsi/hab-scripts/blob/master/hab/cutdown/basicRelayTest_timeDelay.py) - a basic testing script that activates the relay to test it.

# Installing the Scripts

To download the scripts onto the Pi, you’ll have to download [our git repository](https://github.com/wmsi/hab-scripts) of all the various hab scripts using these commands (make sure you’re in the home directory):

	cd ~

	git clone [https://github.com/wmsi/hab-scripts](https://github.com/wmsi/hab-scripts)

Then, you can navigate to the directory where the cutdown-specific scripts are (*there’s nothing to do there, that’s just where the scripts are*):

	cd ~/hab-scripts/hab/cutdown

# Setting the Scripts to run at Startup

The file we want to run at startup is [~/hab-scripts/hab/cutdown/nichromeLauncher.bash](https://github.com/wmsi/hab-scripts/blob/master/hab/cutdown/nichromeLauncher.bash)

**Open ****/etc/rc.local ****with ****sudo nano /etc/rc.local**** and add this line above "****exit 0****":**

	/home/pi/hab-scripts/hab/cutdown/nichromeLauncher.bash

For more detail, follow the [WMSI guide on starting up a file at boot](https://docs.google.com/document/d/1aIX1-GWfFCBw9bCsF-wYT9l991ldAeoEk1jAAZ-uLZQ/edit#). For simplicity's sake, use the first method of putting the command in /etc/rc.local (see short version above).

# Monitoring Script Output

To see the current vs. target altitude the script is set to right now, run this command to monitor the end ("tail") of its log file:

	watch tail ~/cutdown.log

# Configuring Whether to Cut Down after Time vs. Altitude

1. Run sudo nano ~/hab-scripts/hab/cutdown/nichromeLauncher.bash

2. To set the altitude-based script to run, uncomment the command running the  **nichromeCutdownController.py** python file, and re-comment the other line (the only other line)

3. To set the altitude-based script to run, uncomment the command running the  **basicRelayTest_timeDelay.py** python file, and re-comment the other line (the only other line)

# Configuring Cutdown Parameters (Altitude, etc.)

### Setting cutdown altitude

1. Run sudo nano ~/hab-scripts/hab/cutdown/nichromeCutdownController.py to edit the altitude-based cutdown script.

2. Find the constant **MAX_ALTITUDE** and set it as desired **in meters**.

### Setting the number, high duration, and low duration of cutdown activations

1. Run sudo nano ~/hab-scripts/hab/cutdown/nichromeControl.py to edit the nichrome code.

2. To change the **number of pulses**, find the constant **DEF_NICHROME_ACTIVATIONS** and set it as desired.

3. To change the **high (on) duration** during a pulse, find the constant **DEF_NICHROME_HIGH_TIME** and set it as desired **in seconds**

4. To change the **low (off) duration** during a pulse, find the constant **DEF_NICHROME_LOW_TIME** and set it as desired **in seconds**

# Testing the Scripts

There is also a testing script that takes over the role of the Pi In The Sky software and writes "fake" telemetry to the same log file. It is convenient because properties of the flight can be configured easily to do a nearly-realistic cutdown test from the perspective of the script.

### Running the test

1. Make sure the *real *Pi In The Sky (and our tracker script) is off and won’t write to the log files with these commands:

	sudo killall startup

	sudo killall tracker

sudo killall python # for our script, in case started on startup

2. Open the cutdown script directory with cd ~/hab-scripts/hab/cutdown

3. Open up the testing script with sudo nano telemetryGenerator.py to configure the test parameters (see the constants there)

4. Run the cutdown controller script with ./nichromeCutdownController.py

5. Wait for cutdown!

