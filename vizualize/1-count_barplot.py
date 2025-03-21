import matplotlib.pyplot as plt
import seaborn as sns


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
