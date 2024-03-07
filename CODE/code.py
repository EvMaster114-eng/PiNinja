from board import *
import board
import digitalio
import storage

run = True
noRunPin = digitalio.DigitalInOut(GP6)
payloadPins = [
    digitalio.DigitalInOut(GP1),
    digitalio.DigitalInOut(GP2),
    digitalio.DigitalInOut(GP3),
    digitalio.DigitalInOut(GP4),
    digitalio.DigitalInOut(GP5),
]


def pickPayload():
    picked = 0
    running = True

    for i in range(0, len(payloadPins), 1):
        if not running:
            break
        pin = payloadPins[i]

        pin.switch_to_input(digitalio.Pull.UP)

        val = pin.value

        if not pin.value:
            picked = i + 1
            running = False

    if not running:
        print("payload_" + str(picked) + ".py")
        return "payload_" + str(picked) + ".py"
    else:
        print("payload.py")
        return "payload.py"

def start():

    led = digitalio.DigitalInOut(board.LED)
    led.direction = digitalio.Direction.OUTPUT
    led.value = True

    noRunPin.switch_to_input(digitalio.Pull.UP)

    run = noRunPin.value

    print("Run: " + str(run))

    if not run:
        return

    payloadName = pickPayload()

    if payloadName == "payload.py":
        import payload
        payload.main()
    elif payloadName == "payload_1.py":
        import payload_1
        payload_1.main()
    elif payloadName == "payload_2.py":
        import payload_2
        payload_2.main()
    elif payloadName == "payload_3.py":
        import payload_3
        payload_3.main()
    elif payloadName == "payload_4.py":
        import payload_4
        payload_4.main()
    elif payloadName == "payload_5.py":
        import payload_5
        payload_5.main()


start()
