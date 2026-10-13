from machine import Pin
import time

# define the pin connected to the photo interrupter's digital output
photo_interrupter_pin = Pin(28, Pin.In) #connect to GPIO 28

# Main loop to continuously read the sensor
while True:
    if photo_interrupter_pin.value() == 1: # (interrupted = 1)
        print("Object detected!")
    else:
        print("No object detected")
        
    time.sleep(0.1) # Small delay to avoid flooding the serial output
