"""
Use this program to test whether your servo is 180 or 360. Follow the instructions printed to the Thonny shell to diagnose your servo.
This circuit can be wired the same as circuits 7A or 7B in the booklet.
"""
from machine import Pin, PWM
from time import sleep

# Create PWM on GP15 (you can change this pin)
servo = PWM(Pin(0))
servo.freq(50)  # 50Hz for servos

def set_servo_pulse(pulse_us):
    """Set servo pulse width in microseconds"""
    # MicroPython PWM duty is 0-65535 for a 20ms period (50Hz)
    duty = int((pulse_us / 20000) * 65535)
    servo.duty_u16(duty)

print("Servo Test Starting...")
print("Watch the servo behavior:")
print()

# Test 1: Center/Stop position (1500us)
print("Sending 1500us (center/stop)")
print("- 180° servo: should move to center and hold")
print("- 360° servo: should stop spinning")
set_servo_pulse(1500)
sleep(3)

# Test 2: One extreme (1000us)
print("\nSending 1000us")
print("- 180° servo: should move to one end")
print("- 360° servo: should spin one direction")
set_servo_pulse(1000)
sleep(3)

# Test 3: Other extreme (2000us)
print("\nSending 2000us")
print("- 180° servo: should move to other end")
print("- 360° servo: should spin opposite direction")
set_servo_pulse(2000)
sleep(3)

# Return to center/stop
print("\nReturning to 1500us (center/stop)")
set_servo_pulse(1500)
sleep(1)

# Clean up
servo.deinit()
print("\nTest complete!")
