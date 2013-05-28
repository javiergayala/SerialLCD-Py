SerialLCD-Py
============

_Scripts to interact with a Serial LCD_

## Synopsis

While trying to interface my MacBook Pro with a Serial-Enabled LCD Display, I had a heck of a time getting it working.  I was able to get a serial connection going, and could print to the LCD Display, but I couldn't figure out how to do things like clear the display or move the cursor.  This is the result of my efforts.

My setup includes:
  - (2) XBee Series 1 @ 9600bps 8-N-1
  - (1) XBee Breakout Board from Sparkfun
  - (1) XBee USB Explorer Dongle from Sparkfun
  - (1) 16x2 Character Serial LCD Display from Sparkfun
  - (1) MacBook Pro
  - 3.3V Power for standalone XBee w/ Breakout Board
  - 5.0V Power for Serial LCD Display

#### Transmitter
I have the XBee USB Explorer Dongle with an XBee connected to my MacBook Pro via USB.  

#### Receiver
The Serial LCD and the XBee with the Breakout Board are plugged into a common ground.  However, the Serial LCD gets 5V to VDD, and the XBee gets 3.3V to VCC.  The DOUT/TX pin on the standalone XBee is then plugged into the RX pin of the Serial LCD.  The MBP is thus able to send data to the LCD Display via the XBee wirelessly.  **NOTE: It's OK for the XBee to send the Serial LCD a 3.3V signal from it's DOUT/TX to the Serial LCD's RX, but NOT the reverse! Feeding the XBee a 5.0V signal WILL damage it!**


## time-load.py

This script prints the date and time on line 1 of the LCD, and the 1/5/15 minute load average of the MacBookPro on line 2 of the LCD.

