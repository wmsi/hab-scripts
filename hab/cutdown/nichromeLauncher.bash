#!/usr/bin/env bash
# A startup script for the nichromeCutdownController
# Run from /etc/rc.local, i.e.:
#   sudo -u pi /home/pi/hab-scripts/hab/cutdown/nichromeLauncher.bash
# ALSO make sure to set executable with:
#   chmod +x nichromeLauncher.bash
sudo python nichromeCutdownController.py & #&> /home/pi/cutdown.log &
