import numpy as np


coll = [5, -7, -12, 3]
coll_2 = [5, 7, None, None]


def fill_neg_values(click_num):
    array = np.array(click_num)
    return np.abs(array)


def fill_nan_values(click_num):
    array = np.array(click_num, dtype=np.float64)
    array_nan = np.isnan(array)
    return np.where(array_nan, 0, array)


# short


# def fill_neg_values(clicks):
#     return np.where(clicks < 0, abs(clicks), clicks)


# def fill_nan_values(clicks):
#     return np.where(np.isnan(clicks), 0, clicks)


print(fill_neg_values(coll))
print(fill_nan_values(coll_2))
