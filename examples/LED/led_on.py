"""
Modified: 30 Apr 2025
By Maggie Lee

Purpose: Turn an LED on.
Notes : LEDs are polarized! The longer end (+) should be connected to the pin
        and the shorter end (-) should be connected to ground. Also, the resistor 
        used is 330 ohm, but any resistor between 50 and 330 ohm is OK.
"""

from picozero import LED

led = LED(15)  # connects LED to pin 15

while True:
    led.on()  # LED object is turned on
