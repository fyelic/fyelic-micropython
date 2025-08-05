"""
Modified: 30 Apr 2025
By Maggie Lee
Edited by Caroline Vooss

Purpose: Turn an LED on.
Notes : LEDs are polarized! The longer end (+) should be connected to the pin
        and the shorter end (-) should be connected to ground. Also, the resistor 
        used is 330 ohm, but any resistor between 50 and 330 ohm is OK.
"""

from machine import Pin
import time

# Set LED pin to correct number
led_pin = 15
led = Pin(led_pin, Pin.OUT)

while True:
    led.on()  # Turn LED on
    time.sleep(0.5)  # Optional: add delay to see blinking
    led.off()  # Turn LED off
    time.sleep(0.5)  # Optional: add delay to see blinking
