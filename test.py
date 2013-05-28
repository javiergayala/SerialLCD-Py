#!/usr/bin/env python

import serial
import os
from datetime import datetime
import time

clear = '\xFE\x01'
line1 = '\xFE\x80'
line2 = '\xFE\xC0'
square = '\xFF'
invader = '\xFC'

LCD = serial.Serial('/dev/tty.usbserial-AH0015DW', 9600)


def lcdWrite(text1, text2):
    LCD.write(clear)
    LCD.write(line1)
    LCD.write(text1)
    LCD.write(line2)
    LCD.write(text2)
    pass


def getLoad():
    load = os.getloadavg()
    min1 = "%.2f" % load[0]
    min5 = "%.2f" % load[1]
    min10 = "%.2f" % load[2]
    fmtLoad = "%s%s%s%s%s" % (min1, square, min5, square, min10)
    return fmtLoad


def getTime():
    today = datetime.now()
    dateStr = '%s %s/%s %s:%s' % (invader, today.month, today.day, today.hour,
                                  today.minute)
    return dateStr

run = True

while (run is True):
    loadStr = getLoad()
    timeStr = getTime()
    lcdWrite(timeStr, loadStr)
    time.sleep(60)
    pass
