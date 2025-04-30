"""
Modified: 30 Apr 2025
By Maggie Lee

Purpose: Print temperature readings from the TMP36 to the Shell.
Notes : The sensor is polarized, so double check the wiring!

        In this case, the TMP36 is connected to ADC1 (GPIO 27), ground, and
        the 3V3(OUT) pin.
        
        Temperature is printed in Celcius and Fahrenheit. Voltage is also
        printed out for debugging.
"""

from machine import ADC
from time import sleep

tmp36 = ADC(27)  # Set TMP36 as analog input

while True:
    # The ‘read_u16’ returns an unsigned 16-bit integer (between 0 and 65535).
    adc_value = tmp36.read_u16()

    volt = (3.3/65535) * adc_value  # Convert reading to a voltage.
    degC = (100*volt)-50  # Convert voltage to a temperature in Celsius
    # Convert Celsius temperature to Fahrenheit temperature.
    degF = degC * (9.0 / 5.0) + 32.0

    # Print values (temperatures are rounded)
    print(volt)
    print(round(degC, 1))
    print(round(degF, 1))

    sleep(5)  # 5 second delay
