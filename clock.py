# https://www.adafruit.com/product/881
# https://www.adafruit.com/product/3400
# https://github.com/adafruit/Adafruit_CircuitPython_HT16K33
# https://learn.adafruit.com/adafruit-led-backpack/circuitpython-and-python-usage-197dcbfa-4ccf-4b98-a152-3982411df681

import board
from adafruit_ht16k33.segments import Seg7x4
import datetime
import time

# Time update rate
TIME_UPDATE_SECS = 30

# Initialize the 7-segment x 4 "display" global
i2c = board.I2C()
display = Seg7x4(i2c)
display.blink_rate = 0
 
# Set the brightness 0.0-1.0
def brightness(b):
  display.brightness = b

# Given a Python datetime.datetime object, set the display accordingly
def set_time(t, c):
  h = t.hour
  display.brightness = 1.0
  if h < 8 or h > 20:
    display.brightness = 0.05
  if h > 12: h -= 12
  s = ' %d:%02d' % (h, t.minute)
  display.print(s[-5:])
  display.colon = c

def main():
  display.brightness = 1.0
  c = True
  n = -1
  while True:
    # Periodically update the current date and time (in the local timezone)
    n = ((n + 1) % TIME_UPDATE_SECS)
    if 0 == n:
      t = datetime.datetime.now()
    # Update the colon every loop
    c = not c
    set_time(t, c)
    # Loop once a second
    time.sleep(1)

if __name__ == "__main__":
    main()

