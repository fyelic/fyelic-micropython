from machine import Pin, PWM
import time

# Setup: tell the Pico what is plugged into each pin
receiver = Pin(28, Pin.IN) # IR receiver: the Pico listens to it (input)
led = Pin(15, Pin.OUT) # LED: the Pico controls it (output)
emitter = PWM(Pin(16)) # IR transmitter: the Pico controls it (output)
emitter.freq(38000) # Flash the IR light 38,000 times per second (the receiver looks for
this speed)

# Main loop: repeats forever
while True:
# Turn the IR transmitter on (50% on, 50% off)
emitter.duty_u16(32768)
time.sleep(0.001) # Wait 1 millisecond (0.001 seconds)

# The receiver gives 0 when it sees the IR light
if receiver.value() == 0:
led.on() # Light received: turn the LED on
else:
led.off() # No light received: turn the LED off

# Turn the IR transmitter off
emitter.duty_u16(0)
time.sleep(0.001) # Wait 1 millisecond
