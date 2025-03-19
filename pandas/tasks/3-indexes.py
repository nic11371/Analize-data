import pandas as pd


order_path = "./data/Orders.xlsx"


def read_data(path):
    df = pd.read_excel(path, skiprows=2)
    return df


def set_index(df):
    df.index = [f'UUID_{i}' for i in range(1, len(df) + 1)]
    return df


def rename_indexes(df, name_column="UUID_indexes"):
    df.index.name = name_column
    return df


def get_rows(df, count_rows=5):
    return df.iloc[0:count_rows]


print(set_index(read_data))
print(rename_indexes(read_data))
print(get_rows(read_data))
