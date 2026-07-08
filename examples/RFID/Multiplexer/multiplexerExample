"""
Raspberry Pi Pico - MicroPython
TCA9548A I2C Multiplexer + 4x SSD1306 OLED displays

Based on the original Arduino/ESP32 example by Rui Santos
(RandomNerdTutorials.com/tca9548a-i2c-multiplexer-esp32-esp8266-arduino/)

Wiring (default):
  Pico GP0 -> SDA
  Pico GP1 -> SCL
  Pico 3V3 -> VCC (multiplexer + OLEDs)
  Pico GND -> GND

Requires the "ssd1306.py" driver on the Pico's filesystem.
Get it from: https://github.com/micropython/micropython-lib/blob/master/micropython/drivers/display/ssd1306/ssd1306.py
"""

from machine import Pin, I2C
import ssd1306
import time

# ---- Configuration ----
SCREEN_WIDTH = 128
SCREEN_HEIGHT = 64
TCA9548A_ADDR = 0x70
OLED_ADDR = 0x3C

# I2C0 on GP0 (SDA) / GP1 (SCL) - change pins to match your wiring
i2c = I2C(0, sda=Pin(0), scl=Pin(1), freq=400000)


def tca_select(bus):
    """Select the active channel (0-7) on the TCA9548A multiplexer."""
    i2c.writeto(TCA9548A_ADDR, bytes([1 << bus]))
    print(bus)


def draw_big_digit(display, text, x, y, scale, color=1):
    """
    Draw text scaled up, since the ssd1306 driver's built-in text()
    only supports 8x8 pixel characters with no scaling option
    (equivalent to Adafruit_GFX's setTextSize(scale)).
    """
    # Render the text at normal size (8x8 px/char) into a small temporary buffer
    import framebuf
    char_w, char_h = 8, 8
    tmp_w, tmp_h = char_w * len(text), char_h
    tmp = framebuf.FrameBuffer(bytearray((tmp_w + 7) // 8 * tmp_h), tmp_w, tmp_h, framebuf.MONO_HLSB)
    tmp.fill(0)
    tmp.text(text, 0, 0, 1)

    # Blit each "on" pixel from the small buffer as a scaled block
    for yy in range(tmp_h):
        for xx in range(tmp_w):
            if tmp.pixel(xx, yy):
                display.fill_rect(x + xx * scale, y + yy * scale, scale, scale, color)


def init_display(bus, label):
    """Select the multiplexer bus and initialize one SSD1306 display."""
    tca_select(bus)
    try:
        display = ssd1306.SSD1306_I2C(SCREEN_WIDTH, SCREEN_HEIGHT, i2c, addr=OLED_ADDR)
    except OSError:
        print("SSD1306 allocation failed on bus", bus)
        while True:
            pass
    display.fill(0)
    display.show()
    return display


def main():
    # Init OLED displays on buses 2, 3, 4, 5
    displays = {}
    for bus in (2, 3, 4, 5):
        displays[bus] = init_display(bus, bus)

    # Write a number to each OLED
    labels = {2: "1", 3: "2", 4: "3", 5: "4"}
    for bus, text in labels.items():
        tca_select(bus)
        display = displays[bus]
        display.fill(0)
        draw_big_digit(display, text, 45, 10, scale=8, color=1)
        display.show()


main()

while True:
    time.sleep(1)
