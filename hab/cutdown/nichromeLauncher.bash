#!/usr/bin/env bash
# A startup script for the nichromeCutdownController
# Run from /etc/rc.local, i.e.:
#   /home/pi/hab-scripts/hab/cutdown/nichromeLauncher.bash
# ALSO make sure to set executable with:
#   chmod +x nichromeLauncher.bash

# find location of this file; use -u to stop bufferring (so log shows up immediately)
sudo python -u $(dirname "$BASH_SOURCE")/nichromeCutdownController.py &>> /home/pi/cutdown.log &

# If running a time-based test, uncomment this:
# sudo python -u $(dirname "$BASH_SOURCE")/basicRelayTest_timeDelay.py &>> /home/pi/cutdown.log &
