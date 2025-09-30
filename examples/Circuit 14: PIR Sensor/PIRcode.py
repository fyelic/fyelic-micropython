'''
Modified 8 July 2025
By Caroline Vooss

Purpose:      Test a PIR (Passive Infrared Motion Sensor) and print to the shell whether or not motion is detected.
              If it is, an LED will turn on.

Notes:        The PIR should have little knobs at the front that are adjustable. You can remove the Fresnel Lens (white hemisphere)
              to see which knob is which. One controls the time to measure a change, and the other controls the sensitivity required
              to send an impulse. You may need to fuss with these for a little to get a combination that works. Turning the knob CW
              increases the sensitivity/time delay, and CCW decreases the sensitivity/time delay.
         
IMPORTANT:    The PIR sensor takes in 5 volts, rather than the usual 3.3. Make sure you are connecting the power input of the PIR
              directly to the VBUS pin (the first pin to the right of the USB input).
           
Attributions: https://RandomNerdTutorials.com/raspberry-pi-pico-motion-pir-micropython/
              https://lastminuteengineers.com/pir-sensor-arduino-tutorial/
'''
 

from machine import Pin
from time import sleep

# Define the PIR sensor input pin
pir_pin = Pin(0, Pin.IN)

# Define the LED pin (optional, for visual feedback)
led_pin = Pin(1, Pin.OUT)

# Flags to indicate motion detection state
motion_detected = False

motion_stopped_printed = False

# Callback function to handle motion detection
def pir_interrupt(pin):
    global motion_detected
    if pin.value() == 1:  # Rising edge (motion detected)
        motion_detected = True
        led_pin.value(1)  # Turn on the LED
    else:  # Falling edge (motion stopped)
        motion_detected = False
        led_pin.value(0)  # Turn off the LED

# Configure the interrupt on the PIR pin for both rising and falling edges
pir_pin.irq(trigger=(Pin.IRQ_RISING | Pin.IRQ_FALLING), handler=pir_interrupt)

try:  #This won't break the code if nothing is detected
    while True:
        if motion_detected and not motion_stopped_printed:
            print("Motion detected!")
            motion_stopped_printed = True  # Set the flag to indicate motion detected

        elif not motion_detected and motion_stopped_printed:
            print("Motion stopped")
            motion_stopped_printed = False  # Reset the flag

        sleep(0.1)  # Main loop delay

except KeyboardInterrupt:  #You most likely won't encounter this 
    print("Keyboard interrupt")
    pir_pin.irq(trigger=0)  # Disable the interrupt
    led_pin.value(0)  # Turn off the LED
    
except Exception as e:   #You most likely won't encounter this
    print("An unexpected exception occurred:", e)
