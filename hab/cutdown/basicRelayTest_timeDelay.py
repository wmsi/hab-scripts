#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
This is a basic test script to make sure the relay is working with the selected
pin, WITH A TIME DELAY.

It was written by Asher.
Version 1.Git
"""

from nichromeControl import Nichrome
from time import sleep

def main():
    # Wait 5 minutes before starting...
    sleep(300)
    nichrome = Nichrome()
    print(nichrome)
    # We only want 2 activations, so:
    nichrome.activate(2)

main()
