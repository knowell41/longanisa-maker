from controller.utils import ControlSystem
import time

device = ControlSystem(baud=9600, com="COM3")

device.connect()


def on(pin):
    device.sendcommand(command=f"P{pin}LOW\n")


def off(pin):
    device.sendcommand(command=f"P{pin}HIGH\n")


while True:
    on(13)
    time.sleep(1)
    off(13)
    time.sleep(1)
