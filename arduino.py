from serial import Serial


class Arduino:
    def __init__(self, port, baudrate) -> None:
        self.serial = Serial(port, baudrate)

    def read(self) -> None:
        return self.serial.readline().decode('utf-8').rstrip()
