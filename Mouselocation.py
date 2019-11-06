from pynput.mouse import Button, Controller as MSController
import time

"""
Shows the current location of the pointer, updates once per second.
"""

mouse = MSController()
while True:
    print(f"x = {mouse.position[0]}, y = {mouse.position[1]}")
    time.sleep(1)