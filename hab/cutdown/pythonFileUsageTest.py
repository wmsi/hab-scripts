#!/usr/bin/python
import time

# Try running `echo "cats" >> test.txt` to check that
# we can write to the file while it's open and read the new data as well.

with open("test.txt", "r+") as log:
    while True:
        print log.readlines()
        # log.seek(0)
        time.sleep(2)
