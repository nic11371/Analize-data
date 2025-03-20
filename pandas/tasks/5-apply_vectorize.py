import pandas as pd


order_path = "./data/Orders.csv"

# Еще нужна функция read, для преобразования в DataFrame
# BEGIN (write your solution here)

df_clicks = pd.read_csv('./data/Cite_clicks_outliers.csv', index_col=0)


def fill_mean(df):
    df = df.fillna(df.mean())
    return df


def change_type(df):
    df = fill_mean(df)
    df['SHOP1'] = df['SHOP1'].astype(int)
    return df


def get_clicks_statistic(df):
    df = fill_mean(df)
    df['CLICKS_STATISTIC'] = df['SHOP1'].apply(lambda x: 1 if x > 200 else 0)
    return df


def change_statistic(df):
    df = fill_mean(df)
    map_dict = {0: 'bad', 1: 'good'}
    df['CLICKS_STATISTIC'] = df['CLICKS_STATISTIC'].map(map_dict)
    return df
# END
