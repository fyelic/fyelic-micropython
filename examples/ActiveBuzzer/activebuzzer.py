"""
Modified: 9 May 2025
By Maggie Lee

Purpose: Play and stop playing sounds from an active buzzer.
Notes : The active buzzer plays a set sound and can be modified on or off.
        If you want to play a controlled sound, use a Piezo buzzer.   
"""

from machine import Pin
import time

buzzer = Pin(16, Pin.OUT)

while True:
    buzzer.value(1)    # Set buzzer on
    time.sleep(0.5)  # Sleep 0.5s
    buzzer.value(0)    # Set buzzer off
    time.sleep(0.5)  # Sleep 0.5s
