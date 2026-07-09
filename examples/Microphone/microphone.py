import machine
import time

# Configure ADC0 on Pin 26
mic_adc = machine.ADC(26)

print("Starting microphone test... Speak into the ADMP401!")

while True:
    max_val = 0
    min_val = 65535
    
    # Sample the analog signal rapidly for 50 milliseconds
    start_time = time.ticks_ms()
    while time.ticks_diff(time.ticks_ms(), start_time) < 50:
        sample = mic_adc.read_u16()  # Reads a 16-bit integer (0 to 65535)
        
        if sample > max_val:
            max_val = sample
        if sample < min_val:
            min_val = sample
            
    # Calculate peak-to-peak amplitude (sound volume)
    peak_to_peak = max_val - min_val
    
    # Map the peak-to-peak value to a rough visual peak meter
    bars = int(peak_to_peak / 1500)
    print("[" + "#" * bars + " " * (40 - bars) + f"] Vol: {peak_to_peak}")
    
    time.sleep(0.05)
