from machine import Pin, PWM
import time

# Define the GPIO pin connected to the servo's signal wire
SERVO_PIN = 0 

# Initialize PWM on the specified pin
servo_pwm = PWM(Pin(SERVO_PIN))
servo_pwm.freq(50)  # Set the PWM frequency to 50Hz, typical for servos

# Define duty cycle values for controlling the servo
# These values may need adjustment based on your specific servo
STOP_DUTY = 4915  # Duty cycle for stopping the servo (center position)
FORWARD_DUTY = 6553  # Duty cycle for continuous rotation in one direction
REVERSE_DUTY = 3277  # Duty cycle for continuous rotation in the opposite direction

def set_servo_speed(duty_cycle):
    """Sets the duty cycle for the servo."""
    servo_pwm.duty_u16(duty_cycle)

# Main control loop
while True:
    print("Rotating forward...")
    set_servo_speed(FORWARD_DUTY)
    time.sleep(2)  # Rotate forward for 2 seconds

    print("Stopping...")
    set_servo_speed(STOP_DUTY)
    time.sleep(1)  # Stop for 1 second

    print("Rotating in reverse...")
    set_servo_speed(REVERSE_DUTY)
    time.sleep(2)  # Rotate in reverse for 2 seconds

    print("Stopping...")
    set_servo_speed(STOP_DUTY)
    time.sleep(1)  # Stop for 1 second
