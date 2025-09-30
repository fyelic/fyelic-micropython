"""
Modified: 24 May 2025, 15 July 2025
By Maggie Lee
Modified by Caroline Vooss

Purpose: Output primary color presets and secondary color combinations.
"""

from machine import Pin, PWM
import time

# Set up RGB LED pins (adjust pin numbers as needed)
red_pin = 0
green_pin = 1
blue_pin = 2

# Create PWM objects for each color channel
red_led = PWM(Pin(red_pin))
green_led = PWM(Pin(green_pin))
blue_led = PWM(Pin(blue_pin))

# Set PWM frequency (1000 Hz is good for LEDs)
red_led.freq(1000)
green_led.freq(1000)
blue_led.freq(1000)

def set_color(red, green, blue):
    """Set RGB LED color. Values should be 0-255"""
    # Convert 0-255 values to 0-65535 for duty_u16
    red_duty = int(red * 65535 / 255)
    green_duty = int(green * 65535 / 255)
    blue_duty = int(blue * 65535 / 255)
    
    red_led.duty_u16(red_duty)
    green_led.duty_u16(green_duty)
    blue_led.duty_u16(blue_duty)

# Demo: Cycle through different colors
while True:
    # Red
    set_color(255, 0, 0)
    time.sleep(1)
    
    # Green
    set_color(0, 255, 0)
    time.sleep(1)
    
    # Blue
    set_color(0, 0, 255)
    time.sleep(1)
    
    # Yellow (red + green)
    set_color(255, 255, 0)
    time.sleep(1)
    
    # Cyan (green + blue)
    set_color(0, 255, 255)
    time.sleep(1)
    
    # Magenta (red + blue)
    set_color(255, 0, 255)
    time.sleep(1)
    
    # White (all colors)
    set_color(255, 255, 255)
    time.sleep(1)
    
    # Purple
    set_color(128, 0, 128)
    time.sleep(1)
    
    # Orange
    set_color(255, 165, 0)
    time.sleep(1)
    
    # Off
    set_color(0, 0, 0)
    time.sleep(1)
