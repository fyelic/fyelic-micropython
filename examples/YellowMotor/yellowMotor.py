"""
-------------------------------
By Caroline Vooss
Edited on October 6, 2025
Purpose: Control a single motor. Requires a motor driver chip.
Attributions: https://www.kevsrobots.com/learn/micropython_gpio/07_motors.html
-------------------------------
"""
from machine import Pin, PWM
from time import sleep

# Motor control pins
in1 = Pin(0, Pin.OUT)
in2 = Pin(1, Pin.OUT)
ena = PWM(Pin(2))
ena.freq(1000)

def motor_forward(speed=65025):
    in1.high()
    in2.low()
    ena.duty_u16(speed)

def motor_backward(speed=65025):
    in1.low()
    in2.high()
    ena.duty_u16(speed)

def motor_stop():
    in1.low()
    in2.low()
    ena.duty_u16(0)

# Test
motor_forward()
sleep(2)
motor_backward()
sleep(2)
motor_stop()
