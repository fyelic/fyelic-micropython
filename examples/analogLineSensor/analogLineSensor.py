from machine import ADC, Pin
import time

# change the pin number below to match your setup
sensor_pin = ADC(Pin(26)) 

# adjust this threshold based on your environment calibration
# range is 0 to 65535
THRESHOLD = 40000

while True:
    # read analog value
    sensor_value = sensor_pin.read_u16()
    
    # print the value to the shell
    print(f"Analog Value: {sensor_value}")
    
    # if value is greater than the threshold then it is dark enough
    if sensor_value > THRESHOLD:
        print("Status: BLACK line detected")
    else:
        print("Status: WHITE surface detected")
        
    print("-" * 30)
    time.sleep(0.1)
