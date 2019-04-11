import Display as d
from time import sleep

# This is a sample of what you will run to create your display

# Display.py holds your configuration for the pins on your board
# Display.py also holds a variety of display functions, some of which will be sampled here...


while 1:
    """ 
    Logic for display goes here.
    Example:
    """
    d.iterativeCenterFade()
    d.rectangleFadeLeftTop()
    d.flashingRectangleFill(1, 1, 126, 126, d.BLUE, 2)
    d.displayAllChars()
    sleep(0.01)

    d.printMessage("Welcome to the TFT144!", 0, 0, d.BLUE, d.YELLOW)
    sleep(1)

    d.printPleinair()
    d.sleep(3)
