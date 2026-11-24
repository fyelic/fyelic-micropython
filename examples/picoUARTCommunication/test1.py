from machine import Pin

out = Pin(0, Pin.OUT)
inp = Pin(1, Pin.IN, Pin.PULL_DOWN)

out.value(1)
print("Should be 1:", inp.value())
out.value(0)
print("Should be 0:", inp.value())
