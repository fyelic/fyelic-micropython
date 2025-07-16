'''
Modified 16 July 2025
By: Caroline Vooss

Purpose: Wire and code a shift register for use with a series of 8 LEDs
Notes:
      - The 74HC595 shift register is used in this example
      - It is much easier to use bent wires than flexible ones
      - Make sure none of the resistors for the LEDs make contact with each other
      - Full documentation for the 74HC595 can be found here: https://www.ti.com/lit/ds/symlink/sn74hc595.pdf

    
Attrbutions: https://how2electronics.com/shift-register-74hc595-with-raspberry-pi-pico-micropython/

'''


from machine import Pin
from time import sleep
 
latchPin = Pin(3, Pin.OUT)
clockPin = Pin(2, Pin.OUT)
dataPin = Pin(4, Pin.OUT)
 
def update_shift_register(value):
    latchPin.value(0)
    for i in range(8):
        clockPin.value(0)
        dataPin.value((value >> (7 - i)) & 1)
        clockPin.value(1)
    latchPin.value(1)
 
def led_chase():
    for i in range(8):
        leds = 1 << i
        update_shift_register(leds)
        sleep(0.1)  # Adjust delay for speed
 
while True:
    led_chase()
