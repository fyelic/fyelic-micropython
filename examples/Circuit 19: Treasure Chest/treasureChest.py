from machine import Pin, PWM
import time

# Pin setup
tilt_switch = Pin(15, Pin.IN, Pin.PULL_UP)  # Tilt switch with pull-up resistor
buzzer = PWM(Pin(16))  # Passive buzzer

# Set buzzer frequency
buzzer.freq(1000)

print("Treasure Chest Alarm System")
print("Close the chest to arm the system...")

while True:
    # Check if chest is opened (tilt switch activated)
    # Tilt switch reads LOW when level (closed), HIGH when tilted (opened)
    if tilt_switch.value() == 0:  # Chest is opened
        print("ALARM! Chest opened!")
        
        # Sound alarm for 5 seconds
        for i in range(50):  # 50 iterations x 0.1 seconds = 5 seconds
            buzzer.duty_u16(32768)  # Turn buzzer on (50% duty cycle)
            time.sleep(0.05)
            buzzer.duty_u16(0)      # Turn buzzer off
            time.sleep(0.05)
        
        print("Alarm stopped. Close chest to re-arm.")
        
        # Wait for chest to be closed before re-arming
        while tilt_switch.value() == 0:
            time.sleep(0.1)
        
        print("System re-armed!")
    
    else:  # Chest is closed
        buzzer.duty_u16(0)  # Make sure buzzer is off
    
    time.sleep(0.1)  # Small delay
