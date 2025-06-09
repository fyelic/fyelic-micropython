"""
Modified: 31 May 2025
By Maggie Lee

Purpose: Print a photodiode sensor reading to the Shell.
Notes : Make sure the photodiode is connected to an ADC pin.
        In this case, the photodiode is connected to ADC0 (GPIO 26) and 
        the other end is grounded.
        
        Pico's ADC is 12 bits, so the digital signal resolution is 4096 units.
"""
from machine import Pin
import time

# Set photodiode as analog input
photodiode_pin = 26
photodiode = machine.ADC(photodiode_pin)

# Read and print photodiode raw value
while True:
    # The ‘read_u16’ returns an unsigned 16-bit integer (between 0 and 65535).
    print(photodiode.read_u16())
    time.sleep(2)  # 2 second delay
