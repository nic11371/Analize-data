import pandas as pd


df_clicks = pd.read_excel('./data/Cite_clicks.csv', index_col=0)


# BEGIN (write your solution here)
def concat(df_1, df_2):
    union = pd.concat([df_1, df_2], axis=1)
    return union


def join_intersect(df_1, df_2):
    union = df_1.join(df_2, how="inner")
    return union


def merge_all(df_1, df_2):
    union = pd.merge(
        df_1, df_2,
        left_on="day",
        right_on="day",
        how="outer"
    )
    return union
# END
