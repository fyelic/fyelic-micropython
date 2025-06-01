"""
Modified: 31 May 2025
By Maggie Lee

Purpose: Print a flex sensor reading to the Shell.
Notes : Make sure the flex sensor is connected to an ADC pin.
        In this case, the flex sensor is connected to ADC0 (GPIO 26) and 
        the other end is grounded.
        
        The flex sensor needs to be calibrated (change no_flex to reading at
        resting position). Can also change the dividing number to increase
        or decrease sensitivity.
        
        Pico's ADC is 12 bits, so the digital signal resolution is 4096 units.
"""

from machine import ADC, Pin
import time

# Define the pin connected to the flex sensor
# The Raspberry Pi Pico pin GP26 (ADC0) connected to the flex sensor
FLEX_SENSOR_PIN = 26

# Initialize ADC on the specified pin
flex_sensor = ADC(Pin(FLEX_SENSOR_PIN))
no_flex = 104  # Calibrate this based on reading at resting position

# Main loop
while True:
    analog_reading = flex_sensor.read_u16()  # Read the raw analog value (0-65535)
    analog_reading = int(analog_reading/200)  # Divide to stabilize reading

    # Print the raw analog reading
    print("Flex sensor reading = ", analog_reading)

    if analog_reading < no_flex:
        print("flexed backward")
    elif analog_reading > no_flex:
        print("flexed forward")
    else:
        print("no flex")

    time.sleep(1)  # Delay for 1000 milliseconds
