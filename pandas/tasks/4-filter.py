import pandas as pd

order_path = "./data/Orders.csv"

df_clicks = pd.read_csv('./data/Cite_clicks_outliers.csv', index_col=0)


# BEGIN (write your solution here)
def check_nan(df):
    return df.isna().values.sum()


def read_with_nan(order_path, default=0):
    df = pd.read_csv(order_path)
    return df.fillna(default)


def get_clean_df(path):
    df = read_with_nan(path)
    return df.where(df > 0, abs(df))
# END
