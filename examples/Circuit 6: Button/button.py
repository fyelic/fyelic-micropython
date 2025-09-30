"""
Modified: 24 May 2025
By Maggie Lee

Purpose: Print whether a button is pressed or not.
Notes : Version without resistor (Pressed -> 0, Not Pressed -> 1)
        Refer to the correct diagram.

"""
from machine import Pin
import time

# Set up button pin as an input
buttonPin = 14
button = Pin(buttonPin, Pin.IN, Pin.PULL_UP)

while True:
    # 0 is pressed state
    # Print whether button is presssed or not
    if button.value() == 0:
        print("Button Pressed")
    else:
        print("Button Not Pressed")
    time.sleep(1)
