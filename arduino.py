from serial import Serial


class Arduino:
    def __init__(self, port, baudrate) -> None:
        self.serial = Serial(port, baudrate)
        self.record = True

    def read(self) -> None:
        return self.serial.readline().decode('utf-8').rstrip()
        #return "data"

    def set_record(self):
        if self.record == True:
            self.record == False
        elif self.record == False:
            self.record == True
    
    def get_record(self):
        return self.record