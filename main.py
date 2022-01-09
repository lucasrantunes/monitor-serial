import tkinter as tk
from tkinter import filedialog as fd
from arduino import Arduino




window = tk.Tk()
window.geometry("420x420")

arduino = None
arduino_loop = True

def read_loop() -> None:
    global arduino_loop,arduino
    if arduino_loop == True:
        log_text.insert(tk.END, arduino.read() + '\n')
        window.after(500, read_loop)

def start_record() -> None:
    global arduino_loop, arduino
    arduino_loop = True
    arduino = Arduino('/dev/ttyUSB0', 115200)
    window.after(100, read_loop)

def stop_record() -> None:
    global arduino_loop, arduino
    arduino_loop = False
    arduino = None


bottom_frame = tk.Frame(window)
start_button = tk.Button(bottom_frame, text="Start", command=start_record)
stop_button = tk.Button(bottom_frame, text="Stop", command=stop_record)
CheckVar = tk.IntVar(value=1)
auto_save_checkbox = tk.Checkbutton(text="Auto Save", variable=CheckVar)
start_button.pack(side=tk.LEFT)
stop_button.pack(side=tk.RIGHT)
auto_save_checkbox.pack(side=tk.BOTTOM)
bottom_frame.pack(side=tk.BOTTOM)

log_text = tk.Text(window)
log_text.pack()


window.mainloop()
