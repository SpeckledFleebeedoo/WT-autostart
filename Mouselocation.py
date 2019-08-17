from pynput.mouse import Button, Controller as MSController
import time

"""
Shows the current location of the pointer, updates once per second.
"""

mouse = MSController()
while True:
    print('The current pointer position is {0}'.format(
        mouse.position))
    time.sleep(1)