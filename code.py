"""
Example for Pico. Blinks the built-in LED.
"""

# Obtained from:
#
#SPDX-FileCopyrightText: 2021 Kattni Rembor for Adafruit Industries
#
# SPDX-License-Identifier: MIT

import time
import board
import digitalio

# sets LED pin to output
led = digitalio.DigitalInOut(board.LED)
led.direction = digitalio.Direction.OUTPUT

# runs loop turning LED on for 1 second and off for 1 second
while True:
    led.value = True
    time.sleep(1)
    led.value = False
    time.sleep(1)
