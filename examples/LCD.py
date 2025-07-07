'''
Modified: 7 July 2025
By Caroline Vooss

Purpose: Display a simple message on a 16x2 LCD screen
Notes: Two libraries need to be installed prior to running code:
Look for [pico_i2c_lcd.py] and [lcd_api.py] and save to Raspberry Pi.
'''

from picozero import LED
from machine import I2C, Pin
from pico_i2c_lcd import I2cLcd
from time import sleep

i2c = I2C(0, sda=Pin(0), scl=Pin(1), freq=400000)   #Data pin is pin 0, clock pin is pin 1
I2C_ADDR = i2c.scan()[0]
lcd = I2cLcd(i2c, I2C_ADDR, 2, 16)                  #2 rows on LCD, 16 columns

def slowType(lcd, text, delay=0.1):                 #Defines the function to display text
    for i in text:                                  #Reads text as a list, one letter at a time
        lcd.putstr(i)                               #Prints the letter to the LCD
        sleep(delay)                                #Defaults to 0.1 second but can be changed when calling function

while True:
    lcd.show_cursor()                               #Shows cursor
    lcd.blink_cursor_on()                           #Blinks cursor
    slowType(lcd, "Place text here", 0.3)           #Function runs
    sleep(3)                                        #3 second pause
    lcd.blink_cursor_off()                          #Cursor stops blinking
    lcd.hide_cursor()                               #Cursor stops
    sleep(1)                                        #1 second pause
    lcd.clear()                                     #Clears screen