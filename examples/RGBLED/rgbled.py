"""
Modified: 24 May 2025
By Maggie Lee

Purpose: Output red, green, blue, and a custom color.
Notes : The code does not handle invalid inputs (non numbers or numbers < 0 or > 255).

"""
from picozero import RGBLED
from time import sleep

rgb = RGBLED(red=0, green=1, blue=2)

while True:
    rgb.color = (255, 0, 0)
    sleep(0.5)
    rgb.color = (0, 255, 0)
    sleep(0.5)
    rgb.color = (0, 0, 255)
    sleep(0.5)

    print("Output your own color!")
    red = input("Red-ness (0-255)")
    green = input("Green-ness (0-255)")
    blue = input("Blue-ness (0-255)")
    rgb.color = (int(red), int(green), int(blue))
    sleep(5)
