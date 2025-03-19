import os

import pandas as pd


order_path = "./data/Orders.xlsx"

# BEGIN (write your solution here)
def read_data(path):
    df = pd.read_excel(path, skiprows=2)
    return df


def etl(path, default=0):
    df = read_data(path)
    df = df.fillna(default)

    dir_path = '/'.join(path.split('/')[:-1])
    etl_xlsx_path = os.path.join(dir_path, 'Orders_etl.csv')
    df.to_csv(etl_xlsx_path, index=False, sep=',', header=False)
# END

etl(order_path)
