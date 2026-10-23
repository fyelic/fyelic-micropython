from machine import ADC
import time

sensor = ADC(26) # GP26/ADC0
while True:
print(sensor.read_u16()) # 0–65535
time.sleep(0.5)
