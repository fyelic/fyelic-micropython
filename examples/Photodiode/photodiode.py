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

photodiode = machine.ADC(26)  # Set photodiode as analog input

while True:
    print(photodiode.read_u16())
    time.sleep(2)  # 2 second delay
