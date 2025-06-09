"""
Modified: 5 Jun 2025
By Maggie Lee

Purpose: Signify whether the sensor is being touched or not through Shell
         or with the Pico LED.
Notes :  The LED is used as a visual indicator but is not necessary for the
         code to function.
Attributions: Modified from https://docs.sunfounder.com/projects/umsk/en/latest/04_pi_pico/pico_lesson22_touch_sensor.html

"""

from machine import Pin
import time

# Set GPIO 0 as an input pin to read the touch sensor state
touch_sensor_pin = 0
touch_sensor = Pin(touch_sensor_pin, Pin.IN)

# Initialize the onboard LED
led = Pin("LED", Pin.OUT)

while True:
    if touch_sensor.value() == 1:
        led.value(1)  # Turn on the LED
        print("Touch detected!")
    else:
        led.value(0)  # Turn off the LED
        print("No touch detected")

    time.sleep(0.1)
