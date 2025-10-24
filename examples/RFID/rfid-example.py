'''
Modified: 24 October 2025
By Jordan Spencer
Adapted from Microcontrollers Lab

Purpose: Read the ID of a RFID card/tag
Notes: One library needs to be installed prior to running code:
Look for [mfrc522.py]and save to Raspberry Pi.
'''

from mfrc522 import MFRC522
import utime

reader = MFRC522(spi_id=0,sck=2,miso=4,mosi=3,cs=1,rst=0)

print("Bring TAG closer...")
print("")


while True:
    reader.init()
    (stat, tag_type) = reader.request(reader.REQIDL)
    if stat == reader.OK:
        (stat, uid) = reader.SelectTagSN()
        if stat == reader.OK:
            card = int.from_bytes(bytes(uid),"little",False)
            print("CARD ID: "+str(card))
utime.sleep_ms(500) 
