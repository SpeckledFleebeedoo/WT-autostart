from pynput.keyboard import Key, Controller as KBController
from pynput.mouse import Button, Controller as MSController
import time
import os

"""
Installation: Install the module pynput ("pip install pynput" in command prompt) and 
set the pc to turn on at a specific time using the BIOS.
Open the Startup folder by pressing win+r and entering "shell:startup" 
and put in shortcuts to both this program and aces.exe (found in WT folder).

Fill in the coordinates of the necessary clicks where indicated below, the mouselocation.py may 
help finding the correct position.
"""

keyboard = KBController()
mouse = MSController()

mouse.position = (2380, 610) #Location of the click on the "no" button on the promt asking to use the launcher instead
mouse.press(Button.left)
mouse.release(Button.left)

time.sleep(60) #Wait for game to load

keyboard.press(Key.alt) #Close game
keyboard.press(Key.f4)
keyboard.release(Key.alt)
keyboard.release(Key.f4)

#Next block is used to send an email and can safely be removed if unneccessary. Windows mail needs to be configured.

os.system("start mailto:YOURMAIL") #Enter e-mail adress here, starts windows mail.
time.sleep(3)
mouse.position = (670, 290)  #Enter position of mail subject field
mouse.press(Button.left)
mouse.release(Button.left)
keyboard.type("Collected daily reward "+ str(time.asctime(time.localtime(time.time()))))
mouse.position = (1030,100)  #Enter position of send button
mouse.press(Button.left)
mouse.release(Button.left)

#End of mail sender

time.sleep(900) #Time in seconds to shutdown.

os.system("shutdown /p /f") #immediate system shutdown, no prompt