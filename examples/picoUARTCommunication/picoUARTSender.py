from machine import UART, Pin
import time

uart = UART(0, baudrate=9600, tx=Pin(0), rx=Pin(1))

count = 0
while True:
    uart.write(f"Hello {count}\n")
    print("Sent:", count)
    count += 1
    time.sleep(1)
