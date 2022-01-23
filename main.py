import os
from datetime import datetime
from arduino import Arduino
from view import View
import multiprocessing as mp
import subprocess

# arduino variables 
arduino = None

file_name = ""

def read_loop() -> None:
    global arduino
    if(type(arduino) == Arduino):
        if arduino.get_record() == True:
            new_data = arduino.read()
            insert_new_data(new_data)
            view.window.after(10, read_loop)

def insert_new_data(new_data):
    view.insert_text(new_data)
    if view.get_auto_save() == 1:
        file = open(f"log/{file_name}.txt", 'a', encoding='utf-8')
        file.write(f"{new_data}\n")

def start_record() -> None:
    global arduino, file_name
    arduino = Arduino(view.get_port(), view.get_baudrate())
    arduino.set_record()
    file_name = datetime.now().strftime("%d%m%Y_%H%M%S")
    view.window.after(100, read_loop)

def stop_record() -> None:
    global arduino
    if type(arduino) == Arduino:
        arduino.set_record()
        arduino = None

def plot_last_record() -> None:
    if file_name != "":
        #graph = Graph(f"log/{file_name}.txt")
        pass
    else:
        view.error_message("There is no last record.")

def plot_record() -> None:
    #graph = Graph(view.get_file_name())
    subprocess.call(f"python3 graph.py log/{file_name}.txt", shell=True)

def set_directory():
    current_directory = os.getcwd()
    folder_directory = os.path.join(current_directory, r"log") 
    if not os.path.exists(folder_directory):
        os.makedirs(folder_directory)

if __name__ == "__main__":
    view = View(start_record, stop_record, plot_last_record, plot_record)
    set_directory()
    view.set_main_loop()