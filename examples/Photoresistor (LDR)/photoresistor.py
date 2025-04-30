"""
Modified: 30 Apr 2025
By Maggie Lee

Purpose: Print a photoresistor sensor reading to the Shell.
Notes : Make sure the photoresistor is connected to an ADC pin.
        In this case, the photoresistor is connected to ADC1 (GPIO 27) and 
        the other end is grounded.
        
        Pico's ADC is 12 bits, so the digital signal resolution is 4096 units.
"""

from machine import Pin
import time

photoresistor = machine.ADC(27)  # Set photoresistor as analog input

while True:
    # The ‘read_u16’ returns an unsigned 16-bit integer (between 0 and 65535).
    print(photoresistor.read_u16())
    time.sleep(2)  # 2 second delay
