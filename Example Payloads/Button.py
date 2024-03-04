#PiNinja Payload Script
#Title: Button
#Description: Showcases the PiNinja's ability to use external components by opening the minecraft launcher when you press a button

#Imports
import usb_hid
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.mouse import Mouse
from adafruit_hid.keycode import Keycode as key
from adafruit_hid.keyboard_layout_us import KeyboardLayoutUS
from time import sleep

from board import *
import board
import digitalio
#Varibales
kbd = Keyboard(usb_hid.devices)
lay = KeyboardLayoutUS(kbd)
mse = Mouse(usb_hid.devices)

button = digitalio.DigitalInOut(GP15)

def main():
     button.switch_to_input(digitalio.Pull.UP)
     while True:
         val = button.value
         
         if not val:
             kbd.send(key.GUI)
             sleep(0.5)
             lay.write('Minecraft Launcher')
             sleep(0.5)
             kbd.send(key.ENTER)
