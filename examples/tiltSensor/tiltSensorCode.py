"""
Tilt Sensor Test
Modified 8 July 2025
By Caroline Vooss

Purpose: Test a simple circuit with a tilt sensor and LED

Attributes: http://multiwingspan.co.uk/pico.php?page=tilt
"""

from machine import Pin
from time import sleep

tilt = Pin(0, Pin.IN, Pin.PULL_UP)

led = Pin(25, Pin.OUT)

while True:
    led.value(tilt.value())
    sleep(1)
