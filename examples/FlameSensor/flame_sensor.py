"""
Modified: 31 May 2025
By Maggie Lee

Purpose: Print a flame sensor reading to the Shell.

Attributions: Modified from https://docs.sunfounder.com/projects/umsk/en/latest/04_pi_pico/pico_lesson03_flame_sensor.html
"""

from machine import Pin
import time

# Set up flame sensor pin as an input
flame_sensor_pin = 0
flame_sensor = Pin(flame_sensor_pin, Pin.IN)

while True:
    # Flame sensor state is 1 when triggered
    # Print whether triggered or not
    if flame_sensor.value() == 1:
        print("** Fire detected!!! **")
    else:
        print("No Fire detected")

    time.sleep(0.1)
