import os
from datetime import datetime
from arduino import Arduino
from view import View

# arduino variables 
arduino = None

file_name = ""

def read_loop(arduino) -> None:
    if arduino.get_record() == True:
        text = arduino.read()
        view.insert_text(text)
        view.window.after(500, read_loop, arduino)
        if view.get_auto_save() == 1:
            file = open(f"log/{file_name}.txt", 'a', encoding='utf-8')
            file.write(f"{text}\n")

def start_record() -> None:
    global arduino, file_name
    arduino = Arduino(view.get_port(), view.get_baudrate())
    arduino.set_record()
    view.window.after(100, read_loop, arduino)
    file_name = datetime.now().strftime("%d%m%Y_%H%M%S")

def stop_record() -> None:
    global arduino
    arduino.set_record()
    arduino = None

if __name__ == "__main__":
    view = View(start_record, stop_record)
    print(type(view))

    current_directory = os.getcwd()
    folder_directory = os.path.join(current_directory, r"log") 
    if not os.path.exists(folder_directory):
        os.makedirs(folder_directory)

    view.window.mainloop()