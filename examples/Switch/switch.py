"""
Modified: 30 Apr 2025
By Maggie Lee

Purpose: Change the Pico LED based on switch input.
Notes : For the three pin switch in your kit, ground the middle switch pin.
        The data pin can be connected either side of the switch, and that side
        will be considered "on".
        
        Debug Tip: Uncomment print("on") and print("off") in the if statement
        to see the printed state in the Shell. 
"""

from picozero import pico_led, Switch

# Set up switch pin
switch_pin = 15
switch = Switch(switch_pin)

while True:
    if switch.value == True:  # ON state
        print("on")
        # pico_led.on()

    else:  # OFF state
        print("off")
        # pico_led.off()
