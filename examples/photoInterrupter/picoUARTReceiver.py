from machine import UART, Pin

uart = UART(0, baudrate=9600, tx=Pin(0), rx=Pin(1), timeout=100)

print("Starting receiving...")

while True:
    if uart.any():
        msg = uart.readline()
        if msg:
            print("Got:", msg.decode().strip())
