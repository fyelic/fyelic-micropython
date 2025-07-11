"""
Modified: 30 Apr 2025
By Maggie Lee
Edited by Caroline Vooss

Purpose: Blink an LED on and off.
Notes : LEDs are polarized! The longer end (+) should be connected to the pin
        and the shorter end (-) should be connected to ground. Also, the resistor 
        used is 330 ohm, but any resistor between 50 and 330 ohm is OK.
        
        To control the blink timing, use led_on_off.py instead.
"""

from machine import Pin #Tells the code you want to import input/output pins
import time

led_pin = 15 # Set LED pin to correct number
led = Pin(led_pin, Pin.OUT) #sets pin 15 as an output pin

while True:
    led.on()
    time.sleep(1)
    led.off()
    time.sleep(1)
