# graphixPico.py
# For RPi Pico
# https://www.mfitzp.com/tutorials/displaying-images-oled-displays/
# FCM 176 MicroThisMicroThat

import time

from ssd1306 import SSD1306_I2C
import framebuf
from machine import SoftI2C, Pin
i2c = SoftI2C(scl=Pin(9), sda=Pin(8))
display = SSD1306_I2C(128, 64, i2c)

with open('weather_icon-47.pbm','rb') as f:
    mn=f.readline()  # Magic number
    cc=f.readline()  # Creator comment
    if cc.startswith("#"):
        dim=f.readline() # Dimensions
    else:
        dim=cc
        cc='None'
    print(mn)
    print(cc)
    print(dim)    
    data=bytearray(f.read())
fb = framebuf.FrameBuffer(data,50,50, framebuf.MONO_HLSB)
display.fill(0)
display.blit(fb,0,0)
display.show()
