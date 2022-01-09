import tkinter as tk
from tkinter import filedialog as fd
from arduino import Arduino
from datetime import datetime
import os

window = tk.Tk()
window.geometry("420x420")
window.resizable(False,False)
window.title("Serial Monitor")

arduino = None
arduino_loop = True
file_name = ""

def read_loop() -> None:
    global arduino_loop, arduino, auto_save
    if arduino_loop == True:
        text = arduino.read()
        log_text.configure(state=tk.NORMAL)
        log_text.insert(tk.END,  text + '\n')
        log_text.configure(state=tk.DISABLED)
        window.after(500, read_loop)
        if auto_save.get() == 1:
            file = open(f"log/{file_name}.txt", 'a', encoding='utf-8')
            file.write(f"{text}\n")

def start_record() -> None:
    global arduino_loop, arduino, file_name
    arduino_loop = True
    arduino = Arduino(baudrate_text.get("1.0", tk.END).rsplit()[0], int(port_text.get("1.0", tk.END).rsplit()[0]))
    window.after(100, read_loop)
    file_name = datetime.now().strftime("%d%m%Y_%H%M%S")

def stop_record() -> None:
    global arduino_loop, arduino
    arduino_loop = False
    arduino = None

def clear_text() -> None:
    log_text.configure(state=tk.NORMAL)
    log_text.delete("1.0", tk.END)
    log_text.configure(state=tk.DISABLED)


top_frame = tk.Frame(window)
top_frame.pack(side=tk.TOP)
bottom_frame = tk.Frame(window)
bottom_frame.pack(side=tk.BOTTOM)

baudrate_label = tk.Label(top_frame, text="Baudrate: ")
baudrate_label.pack(side=tk.LEFT)
baudrate_text = tk.Text(top_frame, height=1, width=15)
baudrate_text.insert(tk.END, "/dev/ttyUSB0")
baudrate_text.pack(side=tk.LEFT)

port_label = tk.Label(top_frame, text="Port: ")
port_label.pack(side=tk.LEFT)
port_text = tk.Text(top_frame, height=1, width=15)
port_text.insert(tk.INSERT, str(115200))
port_text.pack(side=tk.RIGHT)

log_text = tk.Text(window)
log_text.config(state=tk.DISABLED)
log_text.pack()

start_button = tk.Button(bottom_frame, text="Start", command=start_record)
start_button.pack(side=tk.LEFT)

stop_button = tk.Button(bottom_frame, text="Stop", command=stop_record)
stop_button.pack(side=tk.LEFT)

clear_button = tk.Button(bottom_frame, text="Clear", command=clear_text)
clear_button.pack(side=tk.RIGHT)

auto_save = tk.IntVar(value=1)
auto_save_checkbox = tk.Checkbutton(text="Auto Save", variable=auto_save)
auto_save_checkbox.pack(side=tk.BOTTOM)

current_directory = os.getcwd()
folder_directory = os.path.join(current_directory, r"log") 
if not os.path.exists(folder_directory):
    os.makedirs(folder_directory)

window.mainloop()
