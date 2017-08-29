#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
This is a basic test script to make sure the relay is working with the selected
pin.

It was written by Asher.
Version 1.Git
"""

from nichromeControl import Nichrome

def main():
    nichrome = Nichrome()
    print(nichrome)
    nichrome.activate(20, 1, 0.5)

main()
