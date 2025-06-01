"""
Modified: 31 May 2025
By Maggie Lee

Purpose: Print a flame sensor reading to the Shell.

Attributions: Modified from https://docs.sunfounder.com/projects/umsk/en/latest/04_pi_pico/pico_lesson03_flame_sensor.html
"""

from machine import Pin
import time

# Set GPIO 0 as an input pin to read the flame sensor state
flame_sensor = Pin(0, Pin.IN)

while True:
    if flame_sensor.value() == 1:
        print("** Fire detected!!! **")
    else:
        print("No Fire detected")

    time.sleep(0.1)  # Short delay to reduce CPU usage
