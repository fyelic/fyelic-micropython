"""
Modified: 9 May 2025
By Maggie Lee

Purpose: Determine and print the distance between the ultrasonic distance 
         sensor and an object.
Notes : Distance calculation based on speed of sound (0.0343 cm per 
        microsecond)
        
        Divide total distance by 2 because we only want the distance 
        between sensor to object.

Attributions: https://www.tomshardware.com/how-to/raspberry-pi-pico-ultrasonic-sensor
"""

from machine import Pin
import utime

# Set up trigger pin as an output and echo pin as input
trigger_pin = 3
echo_pin = 2
trigger = Pin(trigger_pin, Pin.OUT)  # Trigger pin sends pulse of current
echo = Pin(echo_pin, Pin.IN)  # Echo pin receives reflected pulse


def ultra():
    # Send out a pulse from trigger pin
    trigger.low()
    utime.sleep_us(2)
    trigger.high()
    utime.sleep_us(5)
    trigger.low()

    # Measure time of signal on vs off
    while echo.value() == 0:
        signaloff = utime.ticks_us()
    while echo.value() == 1:
        signalon = utime.ticks_us()
    timepassed = signalon - signaloff

    # Calculate distance from speed of sound
    distance = (timepassed * 0.0343) / 2
    print("The distance from object is ", distance, "cm")


while True:
    # Run the sensor function
    ultra()
    utime.sleep(1)
