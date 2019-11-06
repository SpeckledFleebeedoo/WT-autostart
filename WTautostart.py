from pynput.keyboard import Key, Controller as KBController
from pynput.mouse import Button, Controller as MSController
from PIL import ImageGrab

import smtplib
import time
import os
from datetime import datetime

"""
Installation: Install the modules pynput and Pillow ("pip install pynput Pillow" in command prompt) and
set the pc to turn on at a specific time using the BIOS.

Open the Startup folder by pressing win+r and entering "shell:startup"
and put in shortcuts to both this program and the War Thunder Launcher.

Fill in the values below to set up the script
"""

#SETUP-------------------------------------------------------------------------------------------------------------
username = "yourmail@gmail.com"     #Email to send from
password = "yourpassword"           #Password of sending account, if using gmail enable less secure apps (https://myaccount.google.com/lesssecureapps) or set an application specific password.
receiver = "receiver@gmail.com"     #Email to send to

#Set a position on the top half of the Play button (not on white text), use mouselocation.py to find values. (These values might work for HD screens, not sure)
mouseposx = 1312
mouseposy = 831

#------------------------------------------------------------------------------------------------------------------

def sendmail(receiver, subject, body, username, password):
    try:
        #Connect to SMTP server and log in
        server = smtplib.SMTP("smtp.gmail.com", 587)        #SMTP server set to gmail, change if using different provider
        server.ehlo()
        server.starttls()
        server.ehlo()
        server.login(username, password)
        
        #Create and send message
        msg = f"Subject: {subject}\n\n{body}"
        server.sendmail(username, receiver, msg)
        
    except:
        print("Sending mail failed")
        pass
    
    finally:
        server.quit()       #Close connection

keyboard = KBController()
mouse = MSController()

time.sleep(5)       #Gives launcher some time to start

#Check color of play button and click if it's red. (Hope it works, it will get stuck in an infinite loop if the position is incorrect.)
mouse.position = (mouseposx, mouseposy)
while True:
    px=ImageGrab.grab().load()
    color=px[mouseposx, mouseposy]
    if color[0] >= 100:
        break
    time.sleep(1)

mouse.press(Button.left)
mouse.release(Button.left)

time.sleep(60)      #Wait for game to load

mouse.position = (1800, 100)    #switch to game window
mouse.press(Button.left)
mouse.release(Button.left)

keyboard.press(Key.alt)     #Close game
keyboard.press(Key.f4)
keyboard.release(Key.alt)
keyboard.release(Key.f4)

#Next block is used to send a comfirmation email and can safely be removed if unneccessary.
subject = "Collected War Thunder daily reward"
body = datetime.now().strftime("%d %B %H:%M")
sendmail(receiver, subject, body, username, password)


time.sleep(900)     #Time in seconds to shutdown. (Gives you a chance to remote in)

os.system("shutdown /p /f")     #System shutdown command
