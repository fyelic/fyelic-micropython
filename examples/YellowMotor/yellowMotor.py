"""
-------------------------------
By Caroline Vooss
Edited on October 6, 2025
Purpose: Control a single motor. Requires a TB6612 motor driver chip.
-------------------------------
"""
from machine import Pin, PWM
from utime import sleep

# Pin setup for TB6612 motor driver
ina1 = Pin(18, Pin.OUT)
ina2 = Pin(17, Pin.OUT)
pwma = PWM(Pin(16))
pwma.freq(1000)

def RotateCW(duty):
    """Rotate motor clockwise at specified duty cycle (0-100)"""
    ina1.value(1)
    ina2.value(0)
    duty_16 = int((duty * 65536) / 100)
    pwma.duty_u16(duty_16)

def RotateCCW(duty):
    """Rotate motor counter-clockwise at specified duty cycle (0-100)"""
    ina1.value(0)
    ina2.value(1)
    duty_16 = int((duty * 65536) / 100)
    pwma.duty_u16(duty_16)
    
def StopMotor():
    """Stop the motor completely"""
    ina1.value(0)
    ina2.value(0)
    pwma.duty_u16(0)

print("DC Motor Control - Enter duty cycle values between 0-100")
print("The motor will rotate CW for 5s, then CCW for 5s, then stop")
print("Press Ctrl+C to exit\n")

while True:
    try:
        duty_cycle = float(input("Enter PWM duty cycle (0-100): "))
        
        # Validate input range
        if 0 <= duty_cycle <= 100:
            print(f"Running at {str(duty_cycle)}% duty cycle")
            
            # Rotate clockwise
            print("  → Rotating CW...")
            RotateCW(duty_cycle)
            sleep(5)
            
            # Rotate counter-clockwise
            print("  → Rotating CCW...")
            RotateCCW(duty_cycle)
            sleep(5)
            
            # Stop motor
            print("  → Stopping motor\n")
            StopMotor()
        else:
            print("Please enter a value between 0 and 100\n")
            
    except ValueError:
        print("Invalid input - please enter a number\n")
    except KeyboardInterrupt:
        print("\n\nStopping motor and exiting...")
        StopMotor()
        break
