# For ESP32
# https://www.mfitzp.com/tutorials/displaying-images-oled-displays/

import time
import ssd1306
import framebuf
from machine import SoftI2C, Pin
i2c = SoftI2C(scl=Pin(18), sda=Pin(19))
display = ssd1306.SSD1306_I2C(128, 64, i2c)

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
fbuf = framebuf.FrameBuffer(data, 32, 32, framebuf.MONO_HLSB)
display.fill(0)
display.framebuf.blit(fbuf, 0, 0)
display.show()