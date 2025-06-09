"""
Modified: 9 May 2025
By Maggie Lee

Purpose: Change the number displayed on a 7 segment from 0-9.
Notes : The wiring diagram shows the wiring for the DP segment, but the pin
        is not configured in the code. 
        
        Review "7segment_detailed.png" to understand the segments (a-g) and 
        related pins.
        
        The number map is used to determine the segments needed to be on and
        off in order to display the respective number.

Attributions: https://electrocredible.com/7-segment-display-with-raspberry-pi-pico/
"""

import machine
import time

# Setup pins as output for 7-segment display segments (a-g)
a_pin = machine.Pin(0, machine.Pin.OUT)
b_pin = machine.Pin(1, machine.Pin.OUT)
c_pin = machine.Pin(2, machine.Pin.OUT)
d_pin = machine.Pin(3, machine.Pin.OUT)
e_pin = machine.Pin(4, machine.Pin.OUT)
f_pin = machine.Pin(5, machine.Pin.OUT)
g_pin = machine.Pin(6, machine.Pin.OUT)

# Create an array of the segments
segments = [
    a_pin,
    b_pin,
    c_pin,
    d_pin,
    e_pin,
    f_pin,
    g_pin
]

# States of the segments for each digit to display numbers 0-9
# State is either ON (1) or OFF (2)
# Structure: [a, b, c, d, e, f, g]
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

# A function to display a given number


def display_number(number):
    # Find the segment states needed to display given number
    segments_values = number_map[number]
    # Loop through each pin and output the correct state
    for i in range(len(segments)):
        segments[i].value(segments_values[i])


while True:
    # Display each digit from 0-9
    for number in range(10):
        display_number(number)
        time.sleep_ms(1000)  # Delay between numbers
