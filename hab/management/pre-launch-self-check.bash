#!/usr/bin/env bash

################################################################################
# Mckenna Cisler - mckennacisler@gmail.com
#
# This script checks various aspects of the HAB's software systems
# to determine if they are launch-ready.
#
# It does not perform any actions; it only reports.
################################################################################

# CONSTANTS
TELEM_LOG="$HOME/pits/tracker/telemetry.txt"
TELEM_DATA_LOG="$HOME/pits/tracker/telemetrydata.txt"
CUTDOWN_LOG="$HOME/cutdown.log"
IMAGE_FOLDER="$HOME/pits/tracker/images"

MAX_IMAGE_FOLDER_SIZE=60000 # bytes
MAX_LOGFILE_SIZE=5000 # bytes

# Useful coloring / styling commands (used as ${bold}**Text**${normal})
bold=$(tput bold)
normal=$(tput sgr0)
RED='\033[0;31m'
GREEN='\033[0;32m'
WHITE='\033[0m'

# functions
function get_file_size() {
  # from https://stackoverflow.com/a/3571834/3155372
  str="$(ls -la $1)"
  arr=($str)
  echo ${arr[4]}
}

function get_folder_size() {
  # from https://stackoverflow.com/a/3571834/3155372
  str="$(du -s $1)"
  arr=($str)
  # convert from KB
  echo $((${arr[0]}*1024))
}

# checks
success=1

clear
echo "
#################################################################
############### Pi In The Sky HAB Systems Check #################
#################################################################
"

# telemetry.txt
printf "
Checking size of telemetry.txt..................................."

telem_txt_size="NONEXISTENT"
telem_txt_size=$(get_file_size $TELEM_LOG)

if  [ ! -f $TELEM_LOG ] || [ $telem_txt_size -gt $MAX_LOGFILE_SIZE ]; then
  success=0
  printf "\rChecking size of telemetry.txt............................${RED}FAILURE${WHITE}\n"
  printf "  ${bold}ERROR: Size of $TELEM_LOG ($telem_txt_size B) exceeds maximium ($MAX_LOGFILE_SIZE B)!${normal}\n\n"
else
  printf "\rChecking size of telemetry.txt............................${GREEN}SUCCESS${WHITE}\n"
  printf "  Size of $TELEM_LOG (${bold}$telem_txt_size B${normal}) is less than maximum ($MAX_LOGFILE_SIZE B)\n"
fi

# telemetrydata.txt
printf "
Checking size of telemetry.txt..................................."

telem_data_txt_size="NONEXISTENT"
telem_data_txt_size=$(get_file_size $TELEM_DATA_LOG)

if [ ! -f $TELEM_DATA_LOG ] || [ $telem_data_txt_size -gt $MAX_LOGFILE_SIZE ]; then
  success=0
  printf "\rChecking size of telemetrydata.txt........................${RED}FAILURE${WHITE}\n"
  printf "  ${bold}ERROR: Size of $TELEM_DATA_LOG ($telem_data_txt_size B) exceeds maximium ($MAX_LOGFILE_SIZE B)!${normal}\n\n"
else
  printf "\rChecking size of telemetrydata.txt........................${GREEN}SUCCESS${WHITE}\n"
  printf "  Size of $TELEM_DATA_LOG (${bold}$telem_data_txt_size B${normal}) is less than maximum ($MAX_LOGFILE_SIZE B)\n"
fi

# cutdown.log
printf "
Checking size of cutdown.log..................................."

cutdown_log_size=="NONEXISTENT"
cutdown_log_size=$(get_file_size $CUTDOWN_LOG)

if [ ! -f $CUTDOWN_LOG ] || [ $cutdown_log_size -gt $MAX_LOGFILE_SIZE ]; then
  success=0
  printf "\rChecking size of cutdown.log..............................${RED}FAILURE${WHITE}\n"
  echo "  ${bold}ERROR: Size of $CUTDOWN_LOG ($cutdown_log_size B) exceeds maximium ($MAX_LOGFILE_SIZE B)!${normal}"
else
  printf "\rChecking size of cutdown.log..............................${GREEN}SUCCESS${WHITE}\n"
  echo "  Size of $CUTDOWN_LOG (${bold}$cutdown_log_size B${normal}) is less than maximum ($MAX_LOGFILE_SIZE B)"
fi

# image folder
printf "
Checking size of tracker images................................."

cutdown_log_size=="NONEXISTENT"
image_folder_size=$(get_folder_size $IMAGE_FOLDER)

if [ ! -d $IMAGE_FOLDER ] || [ $image_folder_size -gt $MAX_IMAGE_FOLDER_SIZE ]; then
  success=0
  printf "\rChecking size of tracker images...........................${RED}FAILURE${WHITE}\n"
  echo "  ${bold}ERROR: Size of $IMAGE_FOLDER ($image_folder_size B) exceeds maximium ($MAX_IMAGE_FOLDER_SIZE B)!${normal}"
else
  printf "\rChecking size of tracker images...........................${GREEN}SUCCESS${WHITE}\n"
  echo "  Size of $IMAGE_FOLDER (${bold}$image_folder_size B${normal}) is less than maximum ($MAX_IMAGE_FOLDER_SIZE B)"
fi

# cutdown script running
printf "
Checking that cutdown program is running........................"

# see if process exists
num_lines=$(ps ax | grep nichromeCutdownController | wc -l)

# +1 becasue there is always one line found, as the grep process shows up in the list
if [ $num_lines -gt 1 ]; then
  printf "\rChecking that cutdown program is running..................${GREEN}SUCCESS${WHITE}\n"
  printf "\nAt least one nichromeCutdownController process found:\n"
# elif [ $num_lines -gt 2 ]; then
  # success=0
  # printf "\rChecking that cutdown program is running..................${RED}FAILURE${WHITE}\n"
  # printf "\n${bold} ERROR: MORE than one nichromeCutdownController process found:${normal}\n"
else
  success=0
  printf "\rChecking that cutdown program is running..................${RED}FAILURE${WHITE}\n"
  printf "\n${bold}ERROR: No nichromeCutdownController process found:${normal}\n"
fi

ps ax | grep nichromeCutdownController
echo

# cutdown script has correct altitude
printf "
Checking that cutdown program has right altitude.................\n"

printf "Latest altitude info: ${bold}$(tail -n 1 $CUTDOWN_LOG)${normal}\n"
read -p "Is the target altitude in the status above correct? [Y/N] " answer

if [ "$answer" == "Y" ] || [ "$answer" == "y" ]; then
  printf "Checking that cutdown program has right altitude..........${GREEN}SUCCESS${WHITE}\n"
else
  printf "Checking that cutdown program has right altitude..........${RED}FAILURE${WHITE}\n"
  success=0
fi

# final check
echo "
#################################################################"
if [ $success -eq 1 ]; then
  printf "##### FINAL SYSTEMS CHECK RESULT....................${GREEN}SUCCESS${WHITE} #####"
else
  printf "##### FINAL SYSTEMS CHECK RESULT....................${RED}FAILURE${WHITE} #####"
fi

echo "
#################################################################

#################################################################
########################### COMPLETED ###########################
#################################################################
"
