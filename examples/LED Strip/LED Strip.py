"""
Modified 7 July 2025
By Caroline Vooss

Purpose: Light up a strip of LED lights, each with a different color
Notes: RGB coloring is used to color the lights. Go to https://www.rapidtables.com/web/color/RGB_Color.html for specific colors and their RGB notation.

Attributions: https://randomnerdtutorials.com/micropython-ws2812b-addressable-rgb-leds-neopixel-esp32-esp8266/
"""
import machine, neopixel

n = 8 #Number of LED pixels on strip
p = 0 #Pin that the LED is connected to on the Pi Pico

np = neopixel.NeoPixel(machine.Pin(p), n)

np[0] = (255, 0, 0)#Red
np[1] = (255, 165, 0) #Orange
np[2] = (255, 255, 0) #Yellow
np[3] = (0, 255, 25)#Green
np[4] = (0, 0, 255)#Blue
np[5] = (128, 0, 128) #Purple
np[6] = (255, 0, 255) #Magenta
np[7] = (255, 255, 255) #White
np.write() #Sends this information to the LED strip
