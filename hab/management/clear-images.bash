#!/usr/bin/env bash

# Script to clear images on PITS tracker
# Mckenna Cisler - mckennacisler@gmail.com

set -e

# Top-level image directory - don't use "~"!
IMG_DIREC="/home/pi/pits/tracker/images"

echo "################## PITS IMAGE REMOVER ##################"
echo 
echo "                    !!! WARNING !!! "
echo " This script will permanantly remove all balloon images!"
echo "                    !!! WARNING !!! "
echo

if [ ! -d "$IMG_DIREC" ]; then
  echo "Image directory '$IMG_DIREC' doesn't exist!"
  exit 1
fi

read -p "Are you sure you would like to do this? [y/n] " answer
if [ "$answer" == "Y" ] || [ "$answer" == "y" ]; then

    read -p "Are you ABSOLUTELY sure you would like to do this? [y/n] " answer    
    if [ "$answer" == "Y" ] || [ "$answer" == "y" ]; then
        
        # even more time for them to quit
        echo "Proceeding..."
        echo "(note: if image directories do not exist or the file path is 
wrong, there will be no error here; check your path!)"
        sleep 2
        
        # remove all images inside folders
        echo "sudo rm -rfv $IMG_DIREC/FULL/*"
        sudo rm -rfv $IMG_DIREC/FULL/*
        echo "sudo rm -rfv $IMG_DIREC/LORA0/*"
        sudo rm -rfv $IMG_DIREC/LORA0/*
        echo "sudo rm -rfv $IMG_DIREC/LORA1/*"
        sudo rm -rfv $IMG_DIREC/LORA1/*
        echo "sudo rm -rfv $IMG_DIREC/ORIGINAL/*"
        sudo rm -rfv $IMG_DIREC/ORIGINAL/*
        echo "sudo rm -rfv $IMG_DIREC/RTTY/*"
        sudo rm -rfv $IMG_DIREC/RTTY/*
        
        echo "Finished"
        exit 0
        
    else
        echo "Aborting..."
        exit 1
    fi 
else
    echo "Aborting..."
    exit 1
fi
