# Piezo Vibration Sensor - Tap Counter

# HOW IT WORKS
#   1. Measure the sensor while it sits still (the "resting level").
#   2. Watch for readings that jump far above that level.
#   3. Each jump is one tap: print the count and blink the LED.

from machine import ADC, Pin
import time

# ----- Settings you can change -----
TAP_SIZE = 3000   # how far above resting counts as a tap (lower = more sensitive)
PAUSE = 0.2       # seconds to wait after a tap so one tap only counts once

# ----- Setup -----
sensor = ADC(Pin(26))       # GP26 reads voltage: 0 = 0 V, 65535 = 3.3 V
led = Pin("LED", Pin.OUT)   # the Pico W's built-in light

# ----- Step 1: Find the resting level -----
print("Measuring resting level... don't touch the disc.")
total = 0
for i in range(100):
    total = total + sensor.read_u16()
    time.sleep(0.01)
resting = total // 100
print("Resting level:", resting)

if resting > 5000:
    print("Warning: resting level is high. Check that S goes to GP26 and - goes to GND.")

# ----- Step 2: Count taps -----
taps = 0
print("Ready! Tap the piezo disc.")

while True:
    reading = sensor.read_u16()

    if reading > resting + TAP_SIZE:
        taps = taps + 1
        print("Tap", taps, "| strength:", reading - resting)
        led.on()
        time.sleep(PAUSE)
        led.off()

