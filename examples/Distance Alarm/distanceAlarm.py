from machine import Pin, I2C
from pico_i2c_lcd import I2cLcd
import utime

# Pin setup
trigger_pin = 2
echo_pin = 3

# Set up trigger pin as output and echo pin as input
trigger = Pin(trigger_pin, Pin.OUT)
echo = Pin(echo_pin, Pin.IN)

# I2C LCD setup
i2c = I2C(0, sda=Pin(0), scl=Pin(1), freq=400000)
I2C_ADDR = i2c.scan()[0]
lcd = I2cLcd(i2c, I2C_ADDR, 2, 16)

def measure_distance():
    """Measure distance using ultrasonic sensor"""
    # Send out a pulse from trigger pin
    trigger.low()
    utime.sleep_us(2)
    trigger.high()
    utime.sleep_us(5)
    trigger.low()
    
    # Measure time of signal on vs off
    while echo.value() == 0:
        signaloff = utime.ticks_us()
    while echo.value() == 1:
        signalon = utime.ticks_us()
    
    # Calculate time passed
    timepassed = signalon - signaloff
    
    # Calculate distance from speed of sound (0.0343 cm/microsecond)
    distance = (timepassed * 0.0343) / 2
    
    return distance

def display_distance(distance):
    """Display distance reading on LCD with status"""
    lcd.clear()
    
    # First line: Distance reading
    lcd.putstr(f"Distance: {distance:.1f}cm")
    
    # Second line: Status message based on distance
    lcd.move_to(0, 1)
    if distance < 5:
        lcd.putstr("TOO CLOSE!")
    elif distance < 15:
        lcd.putstr("WARNING: Near")
    elif distance < 30:
        lcd.putstr("Caution")
    elif distance < 100:
        lcd.putstr("Safe Distance")
    else:
        lcd.putstr("Clear")

def display_startup():
    """Display startup message"""
    lcd.clear()
    lcd.putstr("Distance Monitor")
    lcd.move_to(0, 1)
    lcd.putstr("Initializing...")
    utime.sleep(2)

# Initialize display
print("Distance Monitor Starting...")
display_startup()

# Main monitoring loop
try:
    while True:
        # Measure distance
        distance = measure_distance()
        
        # Display on LCD
        display_distance(distance)
        
        # Print to console for debugging
        print(f"Distance: {distance:.1f} cm")
        
        # Update every 0.2 seconds for smooth operation
        utime.sleep(0.2)

except KeyboardInterrupt:
    print("\nDistance monitor stopped")
    lcd.clear()
    lcd.putstr("Monitor Stopped")
    print("Goodbye!")

except Exception as e:
    print(f"Error occurred: {e}")
    lcd.clear()
    lcd.putstr("ERROR")
    lcd.move_to(0, 1)
    lcd.putstr("Check Wiring")
