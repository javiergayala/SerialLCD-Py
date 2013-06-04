#!/usr/bin/env python
# -*- coding: iso-8859-1 -*-

import serial

# Path to the serial device to use for output
serialDev = '/dev/ttyAMA0'

# Current Speed and New Speed
currSpeed = 9600
newSpeed = 38400

# Define special characters to use with the LCD Display
# First 4 characters represent the command (\xFE = Decimal 254 in Hex)
# Second 4 characters represent the value to set (\x9D = Dec. 157 in Hex)
clear = '\xFE\x01'  # Clear the screen
backOn = '\x7C\x9D'  # Turn backlight brightness to 100%
backOn = '\x7C\x80'  # Turn backlight brightness to 0%
line1 = '\xFE\x80'  # Place cursor at beginning of line 1
line2 = '\xFE\xC0'  # Place cursor at beginning of line 2
bps = []
bps[38400] = '\x7C\x10'  # Set to 38400 baud
bps[19200] = '\x7C\x0F'  # Set to 38400 baud
bps[14400] = '\x7C\x0E'  # Set to 38400 baud
bps[9600] = '\x7C\x0D'  # Set to 38400 baud
bps[4800] = '\x7C\x0C'  # Set to 38400 baud

LCD = serial.Serial(serialDev, currSpeed)


def lcdChSpeed(speed):
    """Write to the LCD Display by clearing it, then writing each line."""
    LCD.write(clear)
    LCD.write(speed)
    pass

lcdChSpeed(bps[newSpeed])

LCD = serial.Serial(serialDev, newSpeed)

LCD.write(clear)
LCD.write(line1)
LCD.write('New Speed:')
LCD.write(line2)
LCD.write(newSpeed)
