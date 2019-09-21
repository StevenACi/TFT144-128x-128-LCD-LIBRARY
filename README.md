
<h3>
V1.7 April 2019

https://github.com/StevenAC

I am updating the display library to include some more prebuilt shapes and animations -while committing further testing
on the printBMP function, and also cleaning up the code for modern IDE's and python 3 coding conventions.

printBMP: we can only read BMP images. included is a sample which will work, however bigger images may fail. 

CE0 or CE1: for my raspberry pi, CE0 was unresponsive, had no choice but to use CE1 pin.

    FOR RED BOARDS:
   
      There is a previous fix to correct a hardware error in a particular version of this display (with a red backplate)
      However, upon testing with a red display, it is my opinion that the manufactures corrected this discrepency. Therefore,
      with a red-back board, it is no longer neccesary to set isRedBoard=True. 
      I left the option open incase someone has an old model of the red TFT144..
 

<h3>
V1.6 April 2015

LCD-TFT-1.44 128x128px. An SPI library for Raspberry Pi or Virtual GPIO.

The "BLACK" 1.44 board from eBay - eg http://www.ebay.com.au/itm/141239781210 - under $4!

The "RED" version. eg. http://www.ebay.com.au/itm/400685907981

RED board has a hardware mistake that preconfigures to 128x160 instead of 128x128. V1.6 of this library corrects for the red board error, but YOU MUST SET "isRedBoard=True" in the TFT144 object constructor. Otherwise some display modes have screen contents jumbled.

Board has inbuilt 5V-3V (2.9?) regulator (which does NOT break out the 3V!!) As far as I can discern, logic level is still 3.3V limit, despite supply is 5V. Currently the code here is designed simply for case of 128x128 pixels. Brian Lavery (C) Oct 2014 brian (at) blavery (dot) com Free software, derived from: (1) ILI9163 128x128 LCD library - parallel I/O AVR C code Copyright (C) 2012 Simon Inns http://www.waitingforfriday.com/index.php/Reverse_Engineering_a_1.5_inch_Photoframe (2) ... then Antares python/parallel Raspberry Pi code: http://www.raspberrypi.org/forums/viewtopic.php?t=58291&p=450201

Added: SPI access, BMP file load, double size fonts, python class, python3/2.7 compatibility Works on: Rasp Pi GPIO, or "virtual GPIO" 3.3V (identical library for both)

On Raspberry Pi, uses SpiDev and RPi.GPIO.
