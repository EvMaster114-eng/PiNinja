#PiNinja Payload Script
#Title:
#Description:

import usb_hid
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.mouse import Mouse
from adafruit_hid.keycode import Keycode as key
from adafruit_hid.keyboard_layout_us import KeyboardLayoutUS
from time import sleep

def main():
    kbd = Keyboard(usb_hid.devices)
    lay = KeyboardLayoutUS(kbd)
    mse = Mouse(usb_hid.devices)

    #Put Your Code Here

