"""
Modified: 31 May 2025
By Maggie Lee

Purpose: Print a force sensor reading to the Shell.
Notes : Make sure the force sensor is connected to an ADC pin.
        In this case, the force sensor is connected to ADC0 (GPIO 26) and 
        the other end is grounded.
        
        Pico's ADC is 12 bits, so the digital signal resolution is 4096 units.
        
Attributions: Modified from https://newbiely.com/tutorials/raspberry-pico/raspberry-pi-pico-force-sensor
"""

from machine import ADC, Pin
import time

# Define the pin connected to the FSR force sensor
# The Raspberry Pi Pico pin GP26 (ADC0) connected to the force sensor
FORCE_SENSOR_PIN = 26

# Initialize ADC on the specified pin
force_sensor = ADC(Pin(FORCE_SENSOR_PIN))

# Main loop
while True:
    analog_reading = force_sensor.read_u16()  # Read the raw analog value (0-65535)

    # Print the raw analog reading
    print("Force sensor reading = ", analog_reading)

    if analog_reading < 6553:       # from 0 to 6552
        print(" -> no pressure")
    elif analog_reading < 13107:    # from 6553 to 13106
        print(" -> light touch")
    elif analog_reading < 32767:    # from 13107 to 32766
        print(" -> light squeeze")
    elif analog_reading < 52428:    # from 32767 to 52427
        print(" -> medium squeeze")
    else:                           # from 52428 to 65535
        print(" -> big squeeze")

    time.sleep(1)  # Delay for 1000 milliseconds
