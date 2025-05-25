"""
Modified: 24 May 2025
By Maggie Lee

Purpose: 
Notes : 

"""
from machine import Pin, PWM
import sys

# Pin setup for right motor
AIN1 = Pin(5, Pin.OUT)
AIN2 = Pin(4, Pin.OUT)
PWMA = PWM(Pin(1))
PWMA.freq(1000)

# Pin setup for left motor
BIN1 = Pin(9, Pin.OUT)
BIN2 = Pin(10, Pin.OUT)
PWMB = PWM(Pin(11))
PWMB.freq(1000)


def set_motor(speed, in1, in2, pwm):
    if speed > 0:
        in1.high()
        in2.low()
    elif speed < 0:
        in1.low()
        in2.high()
    else:
        in1.low()
        in2.low()

    # Convert -65535 to 65535 range to 0-65535 for PWM
    pwm.duty_u16(min(abs(speed), 65535))


def right_motor(speed):
    set_motor(speed, AIN1, AIN2, PWMA)


def left_motor(speed):
    set_motor(speed, BIN1, BIN2, PWMB)

# Helper to get input from serial (USB)


def get_serial_input():
    serial = input("Enter motor speed (-65535 to 65535): ")
    try:
        return int(serial)
    except ValueError:
        return 0


# Main loop
while True:
    motor_speed = get_serial_input()
    print("Motor Speed:", motor_speed)
    right_motor(motor_speed)
    left_motor(motor_speed)
