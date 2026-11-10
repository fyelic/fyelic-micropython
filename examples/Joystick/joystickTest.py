import time
from machine import Pin, ADC, PWM

# ---------------------------------------------------------------------
# Joystick test - same pins and settings as the lockpick game
#   X axis  -> GP26
#   Y axis  -> GP27
#   Button  -> GP28 (active low, internal pull-up)
#   Buzzer  -> GP15 (short click on button press)
# Open the serial console (Thonny / mpremote) to see the output.
# ---------------------------------------------------------------------

DEADZONE = 6000

x_adc = ADC(26)
y_adc = ADC(27)
btn = Pin(28, Pin.IN, Pin.PULL_UP)

buzzer = PWM(Pin(15))
buzzer.freq(2000)
buzzer.duty_u16(0)


def click():
    buzzer.duty_u16(20000)
    time.sleep_ms(20)
    buzzer.duty_u16(0)


def normalize(raw, center):
    offset = raw - center
    if abs(offset) < DEADZONE:
        return 0.0
    return offset / 32768.0


def direction(x, y):
    # Matches the game: stick "up" gives a negative Y value (raises the pin)
    h = "LEFT" if x > 0 else "RIGHT" if x < 0 else ""
    v = "UP" if y < 0 else "DOWN" if y > 0 else ""
    return (v + " " + h).strip() or "CENTER"


# ---------------------------------------------------------------------
# Step 1: measure the resting center (don't touch the stick)
# ---------------------------------------------------------------------
print("Calibrating - leave the joystick alone...")
time.sleep_ms(500)
sx = sy = 0
samples = 100
for _ in range(samples):
    sx += x_adc.read_u16()
    sy += y_adc.read_u16()
    time.sleep_ms(5)
center_x = sx // samples
center_y = sy // samples
print("Measured center  X: {}  Y: {}".format(center_x, center_y))
print("(Each axis now uses its own center.)\n")

# ---------------------------------------------------------------------
# Step 2: live readout
# ---------------------------------------------------------------------
min_x = min_y = 65535
max_x = max_y = 0
last_btn = False

print("Move the stick and press the button. Ctrl+C to stop.\n")

try:
    while True:
        rx = x_adc.read_u16()
        ry = y_adc.read_u16()
        pressed = btn.value() == 0

        min_x, max_x = min(min_x, rx), max(max_x, rx)
        min_y, max_y = min(min_y, ry), max(max_y, ry)

        nx = normalize(rx, center_x)
        ny = normalize(ry, center_y)

        if pressed and not last_btn:
            click()
            print(">>> BUTTON PRESSED")
        elif not pressed and last_btn:
            print(">>> button released")
        last_btn = pressed

        print("X raw:{:5d} norm:{:+.2f} | Y raw:{:5d} norm:{:+.2f} | "
              "BTN:{} | {:<10} | X range {}-{}  Y range {}-{}".format(
                  rx, nx, ry, ny, "ON " if pressed else "off",
                  direction(nx, ny), min_x, max_x, min_y, max_y))

        time.sleep_ms(100)

except KeyboardInterrupt:
    buzzer.duty_u16(0)
    print("\nDone.")
    print("Final X range: {} - {}".format(min_x, max_x))
    print("Final Y range: {} - {}".format(min_y, max_y))
