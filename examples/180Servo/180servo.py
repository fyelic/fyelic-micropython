"""
Modified: 8 May 2025
By Maggie Lee

Purpose: Change the position of a Servo between 0, 90, and 180 degrees.
Notes : The duty cycle needs to be determined based on the specific Servo.
        The default pulse width: 550 - 2400 ms, but read the spec sheet of
        your Servo to determine true range (if applicable)
        
        Duty cycle is calculated as a percentage: (pulse-width/period) * 100
        Period = 1/f, where f is the frequency in Hz (50 Hz in this example)

Attributions: https://randomnerdtutorials.com/raspberry-pi-pico-servo-motor-micropython/
"""

from machine import Pin, PWM
from time import sleep

servo_pin = machine.Pin(0)
servo = PWM(servo_pin)

# Set Duty Cycle for Different Angles
# Default pulse width: 550 - 2400 ms
# Duty cycle (%) = (pulsewidth/period)*100
max_duty = 7864
min_duty = 1802
half_duty = int(max_duty/2)

# Set PWM frequency
frequency = 50
servo.freq(frequency)

while True:
    # Servo at 0 degrees
    servo.duty_u16(min_duty)
    sleep(2)
    # Servo at 90 degrees
    servo.duty_u16(half_duty)
    sleep(2)
    # Servo at 180 degrees
    servo.duty_u16(max_duty)
    sleep(2)
