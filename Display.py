import spidev
from lib_tft144.lib_tft144 import *

from RPi import GPIO

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

RST = 25    # RST may use direct +3V strapping, and then be listed as 0 here. (Soft Reset used instead)
CE = 1    # RPI GPIO : 0 or 1 for CE0 / CE1 number (NOT the pin#)
DC = 24    # Labeled on board as "A0"   Command/Data select
LED = 23    # LED may also be strapped direct to +3V, (and then LED=0 here). LED sinks 10-14 mA @ 3V

spi = spidev.SpiDev()

#  Don't forget the other 2 SPI pins SCK and MOSI (SDA)

TFT = TFT144(GPIO, spi, CE, DC, RST, LED, TFT144.ORIENTATION90, isRedBoard=False)
# TFT = TFT144(GPIO, spi, CE, DC)     # the minimalist version

###########################
# Simplified Method Calls###
# ##//INTERFACE/SECTION//###
###########################

# Defining literals to make writing colors easier

BLUE = TFT.BLUE
LIGHTBLUE = TFT.LIGHTBLUE
GREEN = TFT.GREEN
LIGHTGREEN = TFT.LIGHTGREEN
RED = TFT.RED
PINK = TFT.PINK
BLACK = TFT.BLACK
WHITE = TFT.WHITE
GREY = TFT.GREY
YELLOW = TFT.YELLOW
MAGENTA = TFT.MAGENTA
CYAN = TFT.CYAN

COLORS = [BLUE, LIGHTBLUE, GREEN, LIGHTGREEN, RED, PINK, BLACK, WHITE, GREY, YELLOW, MAGENTA, CYAN]


###########################
#Simplified Method Calls###
####//METHOD SECTION//#####
###########################

def printMessage(strin, xOrigin, yOrigin, fgColor, bgColor):
    print("Message Printed")
    TFT.put_string(strin, xOrigin, yOrigin, fgColor, bgColor, 2)


def printMessageSized(strin, xOrigin, yOrigin, fgColor, bgColor, size):
    print("Message Printed")
    TFT.put_string(strin, xOrigin, yOrigin, fgColor, bgColor, size)


    # PrintBMP is highly untested. Must contain images small enough to be
    # decomposed via the algorithm
def printBMP(bmpURL, sizeX, sizeY):
    print("BMP image:")
    # Prepare your little BMP image first. Correct size. 3 colour (ie 3bytes/pixel format). And rotate it!
    # You may need to tinker to get it right.
    if GPIO.RPI_REVISION > 0:
        if TFT.draw_bmp(bmpURL, sizeX, sizeY):
            sleep(6)
    else:
        # on non-RPI, let's not offend the Foundation
        if TFT.draw_bmp(bmpURL, sizeX, sizeY):
            sleep(6)

    TFT.draw_bmp("bl.bmp")
    sleep(6)


def rectangleFill(x1, y1, x2, y2, color):
    print("Rectangle drawn")
    TFT.draw_filled_rectangle(x1, y1, x2, y2,color)


def flashingRectangleFill(x1, y1, x2, y2, color, seconds):
    seconds = seconds
    while seconds > 0:
        TFT.draw_filled_rectangle(x1, y1, x2, y2, color)
        sleep(0.1)
        TFT.draw_filled_rectangle(x1, y1, x2, y2, WHITE)
        sleep(0.1)
        seconds -= 0.05*3


def rectangle(x1, y1, x2, y2, color):
    TFT.draw_rectangle(x1, y1, x2, y2, color)

def line(x1, y1, x2, y2, color):
    TFT.draw_line(x1, y1, x2, y2, color)

def circle(x1, y1, radius, color):
    TFT.draw_circle(x1, y1, radius, color)


#########################
#MISC METHODS#
###################
#########################
def displayAllChars():
    posx = 0
    posy = 0
    print("Display character set:")
    for i in range(32, 256):
        TFT.put_char(chr(i), posx, posy, TFT.WHITE, TFT.BLACK)
        posx += 6
        if posx >= 121:
            posx = 0
            posy += 8
    for i in range(48, 123):
        TFT.put_char(chr(i), posx, posy, TFT.BLUE, TFT.WHITE)
        posx += 6
        if posx >= 121:
            posx = 0
            posy += 8
    sleep(2)

    print ("Screen blank")
    TFT.led_on(False)
    sleep(2)
    TFT.led_on(True)
    sleep(7)

    TFT.put_string("<<< INVERSION >>>", TFT.textX(2), TFT.textY(15), TFT.YELLOW, TFT.RED)
    # Note can use "character-based" cursor location instead of pixel-based (textX())
    sleep(2)

    print("INVERSION test")
    for i in range(0, 2):
        TFT.invert_screen()
        sleep(0.5)
        TFT.normal_screen()
        sleep(0.5)
    sleep(3)

    TFT.clear_display(TFT.BLUE)

def ballbatanimation():

    print ("Ball & Bat")
    # bat and ball animation
    # (created by original embedded programmer)
    ballX = 64
    ballY = 96
    ballSpeed = 1
    xDir = ballSpeed
    yDir = ballSpeed

    while(1):
        TFT.draw_filled_rectangle(ballX,ballY,ballX+2,ballY+2,TFT.BLACK)
        TFT.draw_filled_rectangle(ballX-2,122,ballX+4,124,TFT.BLACK)
        ballX += xDir
        ballY += yDir
        if (ballX>121):
            xDir = -ballSpeed
        if (ballX<4):
            xDir = ballSpeed
        if (ballY>120):
            yDir = -ballSpeed
        if (ballY<66):
            yDir = ballSpeed
        TFT.draw_filled_rectangle(ballX, ballY, ballX+2, ballY+2, TFT.WHITE)
        TFT.draw_filled_rectangle(ballX-2, 122, ballX+4, 124, TFT.WHITE)


def rectangleFadeLeftTop(start, end, color):
    for i in range(start, end):
        rectangle(i, i, end, end, color)


def printPleinair():
    printBMP("jjj.bmp", 0, 0)


def rectangleCenterFade(color):
    beginx = 64
    beginy = 64
    endx = 64
    endy = 64
    for i in range(0,63):
        beginx -= 1
        beginy += 1
        endx += 1
        endy -= 1
        rectangle(beginx, beginy, endx, endy, color)


def iterativeCenterFade():
    cCount = 0
    while cCount < 11:
        rectangleCenterFade(COLORS[cCount])
        cCount += 1

#############
#MAIN LOOP#
#############
