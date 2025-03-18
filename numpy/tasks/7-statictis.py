import numpy as np


items = np.array([
    [4, 5, 6],
    [3, 1, 4],
    [5, 8, 6],
])

items1 = np.array([
    [4, 5, 6]
])
items2 = np.array([
    [6, 5, 12]
])


def get_iqr(arr):
    return np.percentile(arr, 25), np.percentile(arr, 75)


def get_correlation(arr1, arr2):
    return np.corrcoef(arr1, arr2)[0][1]


print(get_iqr(items))
print(get_correlation(items1, items2))
