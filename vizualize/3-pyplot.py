import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator
import math


# Исходные данные для построения графика
x = list(range(100))
y = [int(10 + 5 * math.sin(i) + 2 * math.sin(10 * i) +
         -2 * math.sin(40 * i) + 2 * math.sin(80 * i)) for i in x]


# BEGIN (write your solution here)
def set_plots_tickers():
    fig, ax = plt.subplots()
    ax.set_title("Daily site visitors", fontsize=12)
    fig.set_size_inches(10, 4)
    ax.plot(x, y,
        color='green',
        linestyle='dashed',
        marker='o',
        linewidth=1,
        markersize=5,
        label='Visitors count'
    )

    ax.xaxis.set_major_locator(MultipleLocator(14))
    ax.xaxis.set_major_formatter('{x:.0f}')

    ax.xaxis.set_minor_locator(MultipleLocator(7))
    ax.xaxis.set_minor_formatter('{x:.0f}')

    ax.yaxis.set_major_locator(MultipleLocator(10))
    ax.yaxis.set_major_formatter('{x:.0f}')

    ax.yaxis.set_minor_locator(MultipleLocator(2))
    ax.yaxis.set_minor_formatter('{x:.0f}')

    ax.tick_params(which='major', length=10)
    ax.tick_params(which='minor', length=4, )

    ax.grid(which='major', color='gray', linewidth=1)
    ax.grid(which='minor', color='gray', linewidth=0.5)

    ax.set_xlabel('Day of the year')
    ax.set_ylabel('Count')
    ax.legend()

    plt.savefig('vizualize/results/pyplot_sinus.png')


set_plots_tickers()
