import tkinter as tk
from tkinter import filedialog as fd
from arduino import Arduino
from datetime import datetime
import os

window = tk.Tk()
window.geometry("420x420")
window.title("Serial Monitor")

arduino = None
arduino_loop = True
file_name = ""

def read_loop() -> None:
    global arduino_loop, arduino, auto_save
    if arduino_loop == True:
        text = arduino.read()
        log_text.insert(tk.END,  text + '\n')
        window.after(500, read_loop)
        if auto_save.get() == 1:
            file = open(f"log/{file_name}.txt", 'a', encoding='utf-8')
            file.write(f"{text}\n")

def start_record() -> None:
    global arduino_loop, arduino, file_name
    arduino_loop = True
    arduino = Arduino('/dev/ttyUSB0', 115200)
    window.after(100, read_loop)
    file_name = datetime.now().strftime("%d%m%Y_%H%M%S")

def stop_record() -> None:
    global arduino_loop, arduino
    arduino_loop = False
    arduino = None


bottom_frame = tk.Frame(window)
start_button = tk.Button(bottom_frame, text="Start", command=start_record)
stop_button = tk.Button(bottom_frame, text="Stop", command=stop_record)
auto_save = tk.IntVar(value=1)
auto_save_checkbox = tk.Checkbutton(text="Auto Save", variable=auto_save)
start_button.pack(side=tk.LEFT)
stop_button.pack(side=tk.RIGHT)
auto_save_checkbox.pack(side=tk.BOTTOM)
bottom_frame.pack(side=tk.BOTTOM)

log_text = tk.Text(window)
log_text.pack()

current_directory = os.getcwd()
folder_directory = os.path.join(current_directory, r"log") 
if not os.path.exists(folder_directory):
    os.makedirs(folder_directory)

window.mainloop()
