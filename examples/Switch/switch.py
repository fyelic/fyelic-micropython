"""
Modified: 30 Apr 2025
By Maggie Lee
Edited by Caroline Vooss

Purpose: Change the Pico LED based on switch input.
Notes : For the three pin switch in your kit, ground the middle switch pin.
        The data pin can be connected either side of the switch, and that side
        will be considered "on".
        
        Debug Tip: Uncomment print("on") and print("off") in the if statement
        to see the printed state in the Shell. 
"""

from machine import Pin
import time

# Set up switch pin
switch_pin = 15
switch = Pin(switch_pin, Pin.IN, Pin.PULL_UP)

# Set up onboard LED (GPIO 25 on Pico)
pico_led = Pin(25, Pin.OUT)

while True:
    if switch.value() == 0:  # Switch pressed (pulled to ground)
        print("on")
        pico_led.on()
    else:  # Switch not pressed (pulled high)
        print("off")
        pico_led.off()
    
    time.sleep(0.1)  # Small delay to avoid excessive polling
