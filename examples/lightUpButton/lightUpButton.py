
"""
Light up button - on when pressed
October 19 2026
By Adam Schaaf

Purpose: Get inputs from a light up button and turn the LED in the button on when the button is 
"""

from machine import Pin
from time import sleep

button = Pin(14, Pin.IN, Pin.PULL_UP)
led = Pin(15, Pin.OUT)

while True:
    if button.value() == 0:   # pressed
        led.on()
    else:
        led.off()
    sleep(0.01)
