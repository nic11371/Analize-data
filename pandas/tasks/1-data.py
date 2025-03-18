import os
import pandas as pd


# BEGIN (write your solution here)
def rename_columns(df):
    df.columns = ['shop_1', 'shop_2', 'shop_3', 'shop_4']
    return df


def fillna_values(df, default=0):
    df = df.fillna(default)
    return df


def etl(orders_path):
    df = pd.read_excel(orders_path)
    df = fillna_values(df, 1)
    rename_columns(df)

    dir_path = '/'.join(orders_path.split('/')[:-1])
    etl_csv_path = os.path.join(dir_path, 'Orders_etl.csv')
    etl_xlsx_path = os.path.join(dir_path, 'Orders_etl.xlsx')

    df.to_csv(etl_csv_path)
    df.to_excel(etl_xlsx_path)
# END
