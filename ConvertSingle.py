# convert single

import glob
from PIL import Image
# from PIL.ImageOps import invert

# define the filename
fn = "weather_icon-49.png"
# open the image
im = Image.open(fn)
# Get just the filename without the extension for later
fn1 = fn[:fn.rfind(".")]
print(f'Working file {fn1}')
# Create a new blank image with a white background
im2 = Image.new('RGBA', im.size, "WHITE")
# Paste the original image into the new image
im2.paste(im, (0, 0), im)
# Convert to RGB format and save a temporary copy
im2.convert('RGB').save('temp.jpg', "JPEG")
# Convert the image to a 1-bit-per-pixel format
im2a = im2.convert('1')
# Resize the image to 32x32 pixels
im3 = im2a.resize((32, 32))
# Save it as a pbm format file
print(im3.format, im3.size, im3.mode)
im3.save(fn1 + '.pbm')
print(im3.format, im3.size, im3.mode)
im4 = Image.open(fn1 + '.pbm')
print(im4.format, im4.size, im4.mode)
im4.close()