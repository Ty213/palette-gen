#!/usr/bin/env python3
from PIL import Image

im = Image.open("testing.jpg")

allColors = {}

width, height = im.size
for x in range(width):
    for y in range(height):
        pixel = im.getpixel((x,y))
        x = pixel in allColors
        if x:
            allColors[pixel] += 1
        else:
            allColors[pixel] = 1


# x = {1: 2, 3: 4, 4: 3, 2: 1, 0: 0}
sortedDict = sorted(allColors, key=allColors.get)
print(sortedDict)