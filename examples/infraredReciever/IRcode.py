"""
Modified 8 July 2025
By Caroline Vooss

Purpose: Test an IR Sensor by turning on a speaker when an object passes in close proximity.

Attributions: https://www.instructables.com/Raspberry-Pi-Pico-and-Proximity-Sensor/
              https://www.youngwonks.com/blog/How-to-use-an-infrared-sensor-with-the-Raspberry-Pi-Pico
"""

from machine import Pin

led = Pin(14, Pin.OUT) #set GPIO-25 pin mode as OUTPUT
sensor = Pin(15, Pin.IN)

while True:
    print(sensor.value())
    if sensor.value() == 0: #read the value of the sensor pin and compare it with 0
        led.value(1)     #set led pin HIGH if sensor pin is LOW
    else:
        led.value(0)     #set led pin HIGH if sensor pin is HIGH
