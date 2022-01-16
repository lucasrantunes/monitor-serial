import tkinter as tk
from tkinter import filedialog as fd
from datetime import datetime
class View:
    def __init__(self, start_record, stop_record, plot_last_record) -> None:
        # setting window
        self.window = tk.Tk()
        self.window.geometry("420x420")
        self.window.resizable(False,False)
        self.window.title("Serial Monitor")

        self.top_frame = tk.Frame(self.window)
        self.top_frame.pack(side=tk.TOP)
        self.bottom_frame = tk.Frame(self.window)
        self.bottom_frame.pack(side=tk.BOTTOM)

        self.baudrate_label = tk.Label(self.top_frame, text="Baudrate: ")
        self.baudrate_label.pack(side=tk.LEFT)
        self.baudrate_text = tk.Text(self.top_frame, height=1, width=15)
        self.baudrate_text.insert(tk.END, str(115200))
        self.baudrate_text.pack(side=tk.LEFT)

        self.port_label = tk.Label(self.top_frame, text="Port: ")
        self.port_label.pack(side=tk.LEFT)
        self.port_text = tk.Text(self.top_frame, height=1, width=15)
        self.port_text.insert(tk.INSERT, "/dev/ttyUSB0")
        self.port_text.pack(side=tk.RIGHT)

        self.log_text = tk.Text(self.window)
        self.log_text.config(state=tk.DISABLED)
        self.log_text.pack()

        self.start_button = tk.Button(self.bottom_frame, 
                                      text="Start", 
                                      command=start_record)
        self.start_button.pack(side=tk.LEFT)

        self.stop_button = tk.Button(self.bottom_frame, 
                                     text="Stop",
                                     command=stop_record)
        self.stop_button.pack(side=tk.LEFT)

        self.clear_button = tk.Button(self.bottom_frame, 
                                      text="Clear", 
                                      command=self.clear_text)
        self.clear_button.pack(side=tk.RIGHT)

        self.menu_bar = tk.Menu(self.window)
        self.file_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.auto_save = tk.IntVar(value=1)
        self.file_menu.add_checkbutton(label="Auto Save", onvalue=1, offvalue=0, variable=self.auto_save)
        self.file_menu.add_command(label="Plot Last Record", command=plot_last_record)
        self.file_menu.add_command(label="Plot Record")
        self.file_menu.add_command(label="Close")

        self.file_menu.add_separator()

        self.file_menu.add_command(label="Exit", command=self.window.quit)
        self.menu_bar.add_cascade(label="File", menu=self.file_menu)
        self.window.config(menu=self.menu_bar)

    def insert_text(self, text) -> None:
        self.log_text.configure(state=tk.NORMAL)
        self.log_text.insert(tk.END,  text + '\n')
        self.log_text.configure(state=tk.DISABLED)

    def get_auto_save(self):
        return self.auto_save.get()
        
    def get_port(self):
        return self.port_text.get("1.0", tk.END).rsplit()[0]

    def get_baudrate(self):
        return int(self.baudrate_text.get("1.0", tk.END).rsplit()[0])

    def clear_text(self) -> None:
        self.log_text.configure(state=tk.NORMAL)
        self.log_text.delete("1.0", tk.END)
        self.log_text.configure(state=tk.DISABLED)

    def set_main_loop(self) -> None:
        self.window.mainloop()