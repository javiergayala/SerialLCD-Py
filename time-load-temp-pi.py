#!/usr/bin/env python
# -*- coding: iso-8859-1 -*-

import serial
import os
from datetime import datetime
import time

# Path to the serial device to use for output
serialDev = '/dev/ttyAMA0'

# Define special characters to use with the LCD Display
# First 4 characters represent the command (\xFE = Decimal 254 in Hex)
# Second 4 characters represent the value to set (\x9D = Dec. 157 in Hex)
clear = '\xFE\x01'  # Clear the screen
backOn = '\x7C\x9D'  # Turn backlight brightness to 100%
backOn = '\x7C\x80'  # Turn backlight brightness to 0%
line1 = '\xFE\x80'  # Place cursor at beginning of line 1
line2 = '\xFE\xC0'  # Place cursor at beginning of line 2
# The following are not commands, but simply characters and therefore only
# contain 1 Hex value instead of 2
square = '\xFF'  # Create character that looks like a filled in block
invader = '\xFC'  # Create char. that looks like space invader
degree = '\xDF'  # Create char. for degree symbol

LCD = serial.Serial(serialDev, 38400)


def getTemp():
    """Grab the CPU temp"""
    rawTemp = open('/sys/class/thermal/thermal_zone0/temp', 'r').readlines()
    tempF = ((float(rawTemp[0].rstrip()) / 1000) * (9.0/5.0)) + 32
    prtTemp = "%.1f%s" % (tempF, degree)
    return prtTemp


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
    dateStr = '%s/%s %s:%s' % (today.month, today.day, today.hour,
                                  format(today.minute, "02d"))
    return dateStr

run = True

while (run is True):
    """Loop to update the display every minute."""
    loadStr = getLoad()
    timeStr = getTime() + ' ' + getTemp()
    lcdWrite(timeStr, loadStr)
    time.sleep(60)
    pass
