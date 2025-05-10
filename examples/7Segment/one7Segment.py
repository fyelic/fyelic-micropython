"""
Modified: 9 May 2025
By Maggie Lee

Purpose: Change the number displayed on a 7 segment from 0-9.
Notes : The wiring diagram shows the wiring for the DP segment, but the pin
        is not configured in the code. 
        
        The number map is used to determine the segments needed to be on and
        off in order to display the respective number.

Attributions: https://electrocredible.com/7-segment-display-with-raspberry-pi-pico/
"""

import machine
import time

# GPIO pins for 7-segment display segments (a-g)
segments = [
    machine.Pin(0, machine.Pin.OUT),
    machine.Pin(1, machine.Pin.OUT),
    machine.Pin(2, machine.Pin.OUT),
    machine.Pin(3, machine.Pin.OUT),
    machine.Pin(4, machine.Pin.OUT),
    machine.Pin(5, machine.Pin.OUT),
    machine.Pin(6, machine.Pin.OUT)
]

# pin states for each digit to display numbers 0-9
number_map = [
    [1, 1, 1, 1, 1, 1, 0],  # 0
    [0, 1, 1, 0, 0, 0, 0],  # 1
    [1, 1, 0, 1, 1, 0, 1],  # 2
    [1, 1, 1, 1, 0, 0, 1],  # 3
    [0, 1, 1, 0, 0, 1, 1],  # 4
    [1, 0, 1, 1, 0, 1, 1],  # 5
    [1, 0, 1, 1, 1, 1, 1],  # 6
    [1, 1, 1, 0, 0, 0, 0],  # 7
    [1, 1, 1, 1, 1, 1, 1],  # 8
    [1, 1, 1, 1, 0, 1, 1]   # 9
]

# function to display a specific number on the 7-segment display


def display_number(number):
    segments_values = number_map[number]
    for i in range(len(segments)):
        segments[i].value(segments_values[i])


while True:
    for number in range(10):
        display_number(number)
        time.sleep_ms(1000)  # Delay between numbers
