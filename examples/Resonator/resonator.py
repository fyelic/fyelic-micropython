# Checks whether the 16 MHz resonator circuit is oscillating.
# Wiring: 74HC14 pin 2 (oscillator output) -> GP26 on the Pico (pin 31)

# How it works:
# The oscillator output switches between 0 V and 3.3 V about 16 million
# times every second. That is much too fast for the Pico to follow one
# switch at a time, so instead we take lots of voltage readings and
# find the average.
#    - If the circuit IS oscillating, the signal is high about half the
#    time and low about half the time, so the average is about half
#    of 3.3 V (around 1.65 V).
#   - If the circuit is NOT oscillating, the output gets stuck at
#    either 0 V or 3.3 V.

from machine import ADC
import time

signal = ADC(26) # GP26 can measure voltage (it is an analog pin)
NUM_READINGS = 1000 # how many readings to average together

while True:
# Add up lots of readings
  total = 0
  for i in range(NUM_READINGS):
    total = total + signal.read_u16()
    # Find the average reading
    average = total / NUM_READINGS
    # read_u16() gives a number from 0 (0 V) to 65535 (3.3 V),
    # so convert it to volts
    voltage = average * 3.3 / 65535
    # An average in the middle means the signal is switching back and forth
  if voltage > 0.5 and voltage < 2.8:
    print("Average voltage:", round(voltage, 2), "V -> The resonator is oscillating!")
    else:
    print("Average voltage:", round(voltage, 2), "V -> No oscillation. Check your wiring.")
    time.sleep(1) # wait 1 second before checking again
