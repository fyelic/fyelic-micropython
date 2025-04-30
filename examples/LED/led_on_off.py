"""
Modified: 30 Apr 2025
By Maggie Lee

Purpose: Blink an LED on and off with 1 second delays.
Notes : LEDs are polarized! The longer end (+) should be connected to the pin
        and the shorter end (-) should be connected to ground. Also, the resistor 
        used is 330 ohm, but any resistor between 50 and 330 ohm is OK.
        
        Import/use sleep instead of sleep_ms to set a delay in s instead of ms.
"""

from picozero import LED
from time import sleep_ms

led = LED(15)

while True:
    led.on()
    sleep_ms(1000)
    led.off()
    sleep_ms(1000)
