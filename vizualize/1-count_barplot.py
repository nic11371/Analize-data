import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


train_data = pd.read_csv('vizualize/fixtures/Wine.csv', index_col=0)
train_data = train_data.fillna(0)
print(train_data.columns.to_list())


# BEGIN (write your solution here)
def get_countplot(df, col_name):
    sns.countplot(x=col_name, data=df)


def get_countplot_with_hue(df, col_name, hue, figsize=(20, 8)):
    plt.figure(figsize=figsize)
    plt.title(f'{col_name} and {hue}', fontsize=16)
    sns.countplot(x=col_name, hue=hue, data=df)


def get_barplot(df, col_name, y_name, figsize=(7, 7)):
    plt.figure(figsize=figsize)
    plt.title(f'Mean {y_name} for {col_name}', fontsize=16)
    sns.barplot(x=col_name, y=y_name, data=df)
# END


get_countplot(train_data, 'country')
