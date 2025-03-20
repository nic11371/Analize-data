import pandas as pd

df_clicks = pd.read_excel('./data/Cite_clicks_info.xlsx', index_col=0)


def get_max(df):
    return df.drop(['Advertising', 'Size'], axis=1).agg('max')


def get_max_for_category(df):
    return df.groupby(['Advertising']).agg("max")


def get_median_for_category(df):
    return df.drop(['Advertising'], axis=1).groupby(['Size']).agg(["median"])
