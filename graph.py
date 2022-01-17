import pandas as pd
import matplotlib.pyplot as plt
class Graph:
    def __init__(self, file_name) -> None:
        self.file_name = file_name
        data = self.read_data()
        self.plot_data(data)

    def read_data(self) -> pd.DataFrame:
        data = pd.read_csv(self.file_name)
        return data

    def plot_data(self, data):
        data.plot(x='tempo')
        plt.xlabel("Time (ms)")
        plt.tight_layout()
        plt.style.use("fivethirtyeight")
        plt.show()

if __name__ == "__main__":
    Graph("log/16012022_140713.txt")