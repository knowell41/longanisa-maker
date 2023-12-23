import serial
import time

# Open a serial port


class ControlSystem:
    def __init__(self, com, baud, timeout=1) -> None:
        self.com = com
        self.baud = baud
        self.timeout = timeout
        self.serial_com = None

    def connect(self):
        self.serial_com = serial.Serial(
            port=self.com, baudrate=self.baud, timeout=self.timeout
        )

    def sendcommand(self, command: str):
        commad_byte = command.encode("utf-8")
        print(commad_byte)
        self.serial_com.write(commad_byte)

    def close(self):
        self.serial_com.close()

    def on(self, pin):
        self.sendcommand(command=f"P{pin}LOW\n")

    def off(self, pin):
        self.sendcommand(command=f"P{pin}HIGH\n")

    def dispense(self, pin, delay=1):
        self.on(pin)
        time.sleep(delay)
        self.off(pin)
