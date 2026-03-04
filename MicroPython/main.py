"""
Created by: Illia
Created on: MAR 2026
This module Temperature
"""

from microbit import *
import random

# our variable for a random number
randoms_numbers = 0

display.clear()
display.show(Image.HAPPY)

while True:
    if button_a.is_pressed():
        randoms_numbers = random.randint(1, 6)
        display.show(str(randoms_numbers))
