import pandas as pd
import matplotlib.pyplot as plt
import sys
import subprocess

class Graph:
    def __init__(self, file_name) -> None:
        self.file_name = file_name
        self.plot_data()

    def read_data(self) -> pd.DataFrame:
        data = pd.read_csv(self.file_name)
        return data

    def plot_data(self):
        data = self.read_data()
        data.plot(x='tempo')
        plt.xlabel("Time (ms)")
        plt.tight_layout()
        plt.style.use("fivethirtyeight")
        plt.show()

if __name__ == "__main__":
    file_name = sys.argv[1:][0]
    Graph(file_name)