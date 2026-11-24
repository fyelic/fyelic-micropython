from machine import UART, Pin
import time

uart = UART(0, baudrate=9600, tx=Pin(0), rx=Pin(1))
uart.write("test\n")
time.sleep(0.1)
print(uart.read())
