from machine import Pin, PWM, ADC
import time
import math

# Pin setup
photoresistor = ADC(26)  # Photoresistor on ADC0 (GPIO 26)
potentiometer = ADC(27)  # Potentiometer on ADC1 (GPIO 27)

# RGB LED pins
red_pin = 0
green_pin = 1
blue_pin = 2

# Create PWM objects for RGB LED
red_led = PWM(Pin(red_pin))
green_led = PWM(Pin(green_pin))
blue_led = PWM(Pin(blue_pin))

# Set PWM frequency
red_led.freq(1000)
green_led.freq(1000)
blue_led.freq(1000)

# Light threshold - adjust this value based on your environment
LIGHT_THRESHOLD = 30000  # Lower values = darker conditions needed to activate

def set_rgb_color(red, green, blue):
    """Set RGB LED color. Values should be 0-255"""
    red_duty = int(red * 65535 / 255)
    green_duty = int(green * 65535 / 255)
    blue_duty = int(blue * 65535 / 255)
    
    red_led.duty_u16(red_duty)
    green_led.duty_u16(green_duty)
    blue_led.duty_u16(blue_duty)

def turn_off_led():
    """Turn off all LED colors"""
    set_rgb_color(0, 0, 0)

def hue_to_rgb(hue):
    """Convert hue (0-360) to RGB values"""
    # Normalize hue to 0-1 range
    h = hue / 360.0
    
    # Simple HSV to RGB conversion with fixed saturation and value
    if h < 1/6:  # Red to Yellow
        r, g, b = 255, int(255 * 6 * h), 0
    elif h < 2/6:  # Yellow to Green
        r, g, b = int(255 * (2 - 6 * h)), 255, 0
    elif h < 3/6:  # Green to Cyan
        r, g, b = 0, 255, int(255 * (6 * h - 2))
    elif h < 4/6:  # Cyan to Blue
        r, g, b = 0, int(255 * (4 - 6 * h)), 255
    elif h < 5/6:  # Blue to Magenta
        r, g, b = int(255 * (6 * h - 4)), 0, 255
    else:  # Magenta to Red
        r, g, b = 255, 0, int(255 * (6 - 6 * h))
    
    return r, g, b

print("RGB Nightlight Starting...")
print("Cover the photoresistor to activate the nightlight")
print("Turn the potentiometer to change colors")

while True:
    # Read sensor values
    light_level = photoresistor.read_u16()
    pot_value = potentiometer.read_u16()
    
    # Convert potentiometer reading to hue (0-360 degrees)
    hue = int(pot_value * 360 / 65535)
    
    # Check if it's dark enough to activate nightlight
    if light_level < LIGHT_THRESHOLD:
        # It's dark - turn on the nightlight
        r, g, b = hue_to_rgb(hue)
        set_rgb_color(r, g, b)
        print(f"Nightlight ON - Light: {light_level}, Hue: {hue}°, RGB: ({r},{g},{b})")
    else:
        # It's bright - turn off the nightlight
        turn_off_led()
        print(f"Nightlight OFF - Light: {light_level} (too bright)")
    
    time.sleep(0.1)  # Small delay for smooth operation
