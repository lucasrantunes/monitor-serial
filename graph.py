from matplotlib.animation import FuncAnimation
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import style
import sys

def plot_data(data):
    column_number = len(data.columns)
    time_column = column_number - 1
    x = data[data.columns[time_column]].tolist()
    column = 0
    plt.cla()
    while column < column_number - 1:
        y = data[data.columns[column]].tolist()
        line_label = data.columns[column]
        plt.plot(x, y, label=f"{line_label}")
        plt.legend(loc="upper left")
        column += 1

def read_data(file_name) -> pd.DataFrame:
    data = pd.read_csv(file_name)
    tail = data.tail(100)
    return tail

def update_plot(i):
    global file_name
    data = read_data(file_name)
    plot_data(data)

def main():
    global file_name
    file_name = sys.argv[1:][0]
    data = read_data(file_name)
    plot_data(data)
    ani = FuncAnimation(plt.gcf(), update_plot, interval=200)
    plt.tight_layout()
    plt.show()
    
if __name__ == "__main__":
    main()