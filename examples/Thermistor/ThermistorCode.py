"""
Thermistor Test
Modified 9 July 2025
By Caroline Vooss

Purpose: Test a thermistor to measure the temperature of a room in Celsius and Kelvin
Attributes: Lafvin Thermistor Tutorial

"""
import machine
import time
import math

adc = machine.ADC(26) #Pin thermistor is connected to

while True:
    adcValue = adc.read_u16() #Measures the voltage going through the thermistor
    voltage = adcValue / 65535.0 * 3.3 #ADC (analog-to-digital converter) value is proportional to the voltage passed through
    Rt = 10 * voltage / (3.3 - voltage) #Rt is the resistance measured in the new temperature
    tempK = (1 / (1 / (273.15 + 25) + (math.log(Rt / 10)) / 3950)) #This equation is used to find the temperature in Kelvin
    tempC = int(tempK - 273.15) #This equation is used to find the temperature in Celsius
    print("ADC Value: ", adcValue, "Voltage: %0.2f"%voltage,"Temperature: ",tempC,"C")
    time.sleep(1)
    
