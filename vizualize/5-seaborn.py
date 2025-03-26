import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd


# Готовим датафрейм
df = pd.read_csv('taxi_orders.csv')
df['datetime'] = pd.to_datetime(df['datetime'])
df['hour'] = df['datetime'].dt.hour


# BEGIN (write your solution here)
def get_orders():
    sns.barplot(
        x='hour',
        y='num_orders',
        palette='hls',
        data=df
    )
    plt.title('Количество заказов такси по часам')
    plt.grid()
    plt.xlabel('Часы')
    plt.ylabel('Количество заказов')
    plt.savefig('vizualize/results/seaborn.png')
# END
