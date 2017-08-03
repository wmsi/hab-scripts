#!/bin/sh
#altLauncher.sh
#start pigpio, then navigate to home directory, then execute python script

sudo pigpiod

cd /
cd home/pi
sudo python altitudeParser.py
cd /

