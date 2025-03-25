import matplotlib.pyplot as plt
from sklearn.datasets import load_wine


# Исходные данные для построения графика
data = load_wine()

x = data.data

print("Data example:")
print(x[0])
# => Data example:
# [1.423e+01 1.710e+00 2.430e+00 1.560e+01 1.270e+02 2.800e+00 3.060e+00
#  2.800e-01 2.290e+00 5.640e+00 1.040e+00 3.920e+00 1.065e+03]

print("Number of features:")
print(len(x[0]))
# => Number of features:
# 13

print("Data feature names:")
print(data.feature_names)
# => Data feature names:
# [
#   'alcohol', 'malic_acid', 'ash',
#   'alcalinity_of_ash', 'magnesium',
#   'total_phenols', 'flavanoids', 'nonflavanoid_phenols',
#   'proanthocyanins', 'color_intensity', 'hue',
#   'od280/od315_of_diluted_wines', 'proline'
# ]


# BEGIN (write your solution here)
def get_hist_plots():
    fig, ax = plt.subplots(3, 5)
    fig.set_size_inches(20, 12)
    fig.suptitle("Features of wine")
    n = 13
    for pos in range(n):
        feature_name = data.feature_names[pos]
        ax_position = ax[pos // 5, pos % 5]
        ax_position.hist(x[:, pos], bins=20, linewidth=0.5, label=feature_name)
        ax_position.legend()
        ax_position.grid()
    plt.savefig('vizualize/results/static_hist.png')


def get_violinplot_plots():
    fig, ax = plt.subplots(3, 5)
    fig.set_size_inches(20, 12)
    fig.suptitle("Features of wine")
    n = 13
    for pos in range(n):
        feature_name = data.feature_names[pos]
        ax_position = ax[pos // 5, pos % 5]
        ax_position.set_title(feature_name)
        ax_position.violinplot(x[:, pos], positions=[0], showmedians=True)
        ax_position.grid()
    plt.savefig('vizualize/results/static_violin_median.png')
# END
