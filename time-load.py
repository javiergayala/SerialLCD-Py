#!/usr/bin/env python

import serial
import os
from datetime import datetime
import time

# Path to the serial device to use for output
serialDev = '/dev/tty.usbserial-AH0015DW'

# Define special characters to use with the LCD Display
clear = '\xFE\x01'  # Clear the screen
line1 = '\xFE\x80'  # Place cursor at beginning of line 1
line2 = '\xFE\xC0'  # Place cursor at beginning of line 2
square = '\xFF'  # Create character that looks like a filled in block
invader = '\xFC'  # Create char. that looks like space invader

LCD = serial.Serial(serialDev, 9600)


def lcdWrite(text1, text2):
    """Write to the LCD Display by clearing it, then writing each line."""
    LCD.write(clear)
    LCD.write(line1)
    LCD.write(text1)
    LCD.write(line2)
    LCD.write(text2)
    pass


def getLoad():
    """Get the load avg. then format it for the LCD Display"""
    load = os.getloadavg()
    min1 = "%.2f" % load[0]
    min5 = "%.2f" % load[1]
    min10 = "%.2f" % load[2]
    fmtLoad = "%s%s%s%s%s" % (min1, square, min5, square, min10)
    return fmtLoad


def getTime():
    """Get the date and time and format it for the LCD Display"""
    today = datetime.now()
    dateStr = '%s %s/%s %s:%s' % (invader, today.month, today.day, today.hour,
                                  format(today.minute, "02d"))
    return dateStr

run = True

while (run is True):
    """Loop to update the display every minute."""
    loadStr = getLoad()
    timeStr = getTime()
    lcdWrite(timeStr, loadStr)
    time.sleep(60)
    pass
