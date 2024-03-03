#PiNinja Payload Script
#Title: Hello World!
#Author: EvMaster114
#Description: Simple hello world script

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
    kbd.send(key.GUI, key.R)
    sleep(0.5)
    lay.write("notepad")
    sleep(0.5)
    kbd.send(key.ENTER)
    sleep(0.5)
    kbd.send(key.LEFT_CONTROL, key.A)
    sleep(0.5)
    kbd.send(key.BACKSPACE)
    sleep(0.5)
    lay.write("Hello World!")


