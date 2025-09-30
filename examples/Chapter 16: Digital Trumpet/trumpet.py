from machine import Pin, PWM
import time

# Pin setup
buzzer_pin = 0
button1_pin = 13
button2_pin = 14
button3_pin = 15

# Create PWM object for buzzer
buzzer = PWM(Pin(buzzer_pin))
buzzer.freq(1000)  # Set initial frequency

# Create button objects with pull-up resistors
button1 = Pin(button1_pin, Pin.IN, Pin.PULL_UP)
button2 = Pin(button2_pin, Pin.IN, Pin.PULL_UP)
button3 = Pin(button3_pin, Pin.IN, Pin.PULL_UP)

# Musical note frequencies (in Hz)
# Each button combination produces a different note
notes = {
    # Single button presses
    (False, False, False): 0,      # No buttons - silence
    (True, False, False): 262,     # Button 1 - C4
    (False, True, False): 294,     # Button 2 - D4
    (False, False, True): 330,     # Button 3 - E4
    
    # Two button combinations
    (True, True, False): 349,      # Buttons 1+2 - F4
    (True, False, True): 392,      # Buttons 1+3 - G4
    (False, True, True): 440,      # Buttons 2+3 - A4
    
    # All three buttons
    (True, True, True): 494,       # Buttons 1+2+3 - B4
}

def read_buttons():
    """Read button states and return as tuple"""
    # Note: Buttons are active LOW with pull-up resistors. This is why the 'not' is there.
    btn1_pressed = not button1.value()
    btn2_pressed = not button2.value()
    btn3_pressed = not button3.value()
    
    return (btn1_pressed, btn2_pressed, btn3_pressed)

def play_note(frequency):
    """Play a note at given frequency"""
    if frequency > 0:
        buzzer.freq(frequency)
        buzzer.duty_u16(32768)  # 50% duty cycle for clear tone
    else:
        buzzer.duty_u16(0)      # Turn off buzzer for silence

def get_note_name(button_combo):
    """Get note name for display"""
    note_names = {
        (False, False, False): "Silence",
        (True, False, False): "C4",
        (False, True, False): "D4",
        (False, False, True): "E4",
        (True, True, False): "F4",
        (True, False, True): "G4",
        (False, True, True): "A4",
        (True, True, True): "B4",
    }
    return note_names.get(button_combo, "Unknown")

print("Digital Trumpet Ready!")
print("Press buttons to play notes:")
print("Button 1: C4")
print("Button 2: D4") 
print("Button 3: E4")
print("Button 1+2: F4")
print("Button 1+3: G4")
print("Button 2+3: A4")
print("Button 1+2+3: B4")
print("Press Ctrl+C to stop")

# Keep track of previous button state to reduce console spam
previous_buttons = (False, False, False)

    while True:
        # Read current button states
        current_buttons = read_buttons()
        
        # Only update if button state changed
        if current_buttons != previous_buttons:
            # Get frequency for this button combination
            frequency = notes.get(current_buttons, 0)
            
            # Play the note
            play_note(frequency)
            
            # Print current note (optional - comment out if too much output)
            note_name = get_note_name(current_buttons)
            if frequency > 0:
                print(f"Playing: {note_name} ({frequency} Hz)")
            else:
                print("Silence")
            
            # Update previous state
            previous_buttons = current_buttons
        
        time.sleep(0.05)  # Small delay for responsive but not overwhelming updates
