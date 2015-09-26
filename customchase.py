#!/usr/bin/env python
import apa102
import buttons
from config import numPixels
from sys import argv
from time import sleep

if len(argv)>1:
  pause = float(argv[1])
else:
  pause = 0.01;

if len(argv)>2:
  brite = int(argv[2])
else:
  brite = 2;

if pause < 0:
  pause = 0
if pause > 10:
  pause = 10


if brite < 2:
  brite = 2

if brite > 31:
  brite = 31

"""
Chase a segment of LEDs round the strip
"""
def shutdown():
  print 22
try:
  strip = apa102.APA102(numPixels, brite) # Low brightness (2 out of max. 31)

  buttons.init(shutdown)

  while True:  # Loop forever
    for j in range(256): # Change the color through the color wheel
      for q in range(7):
        # For smooth entry and exit, the loop must start and end with hidden pixels
        # This way, the pixels "roll in" and "slide out" of the strip
        for i in range(-5, numPixels, 7): # Each segment is 7 LEDs long
          index = strip.wheel( (i + j) % 255)
          strip.setPixelRGB(i+q, 0);
          strip.setPixelRGB(i+q+1, 0);
          strip.setPixelRGB(i+q+2, index);
          strip.setPixelRGB(i+q+3, index);
          strip.setPixelRGB(i+q+4, index);
          strip.setPixelRGB(i+q+5, index);
          strip.setPixelRGB(i+q+6, index); # Wrap, if we are at the end of the strip
        strip.show()    
        sleep(pause)
except KeyboardInterrupt:  # Abbruch...
  print('Interrupted...')
  strip.clearStrip()
  print('Strip cleared')
  strip.cleanup()
  print('SPI closed')
