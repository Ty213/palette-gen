#!/usr/bin/env python3
from PIL import Image

im = Image.open("testing.jpeg")

width, height = im.size

allColors = {}

for x in range(width):
    for y in range(height):
        pixel = im.getpixel((x,y))
        x = pixel in allColors
        if x:
            allColors[pixel] += 1
        else:
            allColors[pixel] = 1

sortedDict = sorted(allColors, key=allColors.get)
print('this is the sorrted dict',sortedDict)
