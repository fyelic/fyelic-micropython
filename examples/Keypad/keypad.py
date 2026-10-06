from machine import Pin
from time import sleep

print("Starting")

# Keypad layout
keys = [
    ['1', '2', '3', 'A'],
    ['4', '5', '6', 'B'],
    ['7', '8', '9', 'C'],
    ['*', '0', '#', 'D']
]

# GPIO pins connected to keypad rows
row_pins = [26, 22, 21, 20]
# Set rows as outputs
row1 = Pin(26, Pin.OUT)
row2 = Pin(22, Pin.OUT)
row3 = Pin(21, Pin.OUT)
row4 = Pin(20, Pin.OUT)
rows = [row1, row2, row3, row4]

# GPIO pins connected to keypad columns
col_pins = [19, 18, 17, 16]
# Set columns as inputs with pull-down resistors, this makes sure it is always ground when not pressed
col1 = Pin(19, Pin.IN, Pin.PULL_DOWN)
col2 = Pin(18, Pin.IN, Pin.PULL_DOWN)
col3 = Pin(17, Pin.IN, Pin.PULL_DOWN)
col4 = Pin(16, Pin.IN, Pin.PULL_DOWN)
cols = [col1, col2, col3, col4]




def get_key():
    for row in range(4):

        # Turn on one row
        rows[row].value(1)

        # Check each column
        for col in range(4):
            if cols[col].value() == 1:

                # Turn row back off
                rows[row].value(0)

                return keys[row][col]

        # Turn row back off
        rows[row].value(0)

    return None


while True:
    key = get_key()

    if key is not None:
        print("Key pressed:", key)

        # Wait for the key to be released
        while get_key() is not None:
            sleep(0.01)

    sleep(0.01)
