import pandas as pd
import matplotlib.pyplot as plt


order_path = "./data/Orders.csv"


# BEGIN (write your solution here)
def read_and_plot(path):
    df = pd.read_csv(path, sep=',', index_col=0)
    df.plot()
    plt.show()


def clean_plot(path):
    df = pd.read_csv(path, sep=',', index_col=0)
    df = df[df > 200]
    df = df.fillna(df.min().min())
    df.plot()
    plt.show()


def max_plot(path):
    df = pd.read_csv(path, sep=',', index_col=0)
    df = df[df > 200]
    df = df.fillna(df.min().min())
    df.max().plot(kind="pie")
    plt.show()
# END
