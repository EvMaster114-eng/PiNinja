from board import *
import board
import digitalio
import storage
import supervisor

showStorage = False
storagePins = [
    digitalio.DigitalInOut(GP16),
    digitalio.DigitalInOut(GP17),
    digitalio.DigitalInOut(GP18),
    digitalio.DigitalInOut(GP19),
    digitalio.DigitalInOut(GP20),
    digitalio.DigitalInOut(GP21),
    digitalio.DigitalInOut(GP22),
    digitalio.DigitalInOut(GP26),
    digitalio.DigitalInOut(GP27),
    digitalio.DigitalInOut(GP28),
]

supervisor.runtime.autoreload = False

for pin in storagePins:
    pin.switch_to_input(digitalio.Pull.UP)

    if not pin.value:
        showStorage = True

if not showStorage:
    storage.disable_usb_drive()
