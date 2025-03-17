import numpy as np


orders_values = [
    [7, 1, -7, None],
    [1000, 2, 4, None],
    [3, None, 503, 3],
    [8, 12, 8, 7],
    [15, 11, None, 9],
    [None, 18, 17, -21],
    [252, 16, 25, 17]
]

orders = np.array(orders_values, dtype=np.float64)


def get_negative_values_number(click_values):
    return len(click_values[click_values < 0])


def get_nan_values_number(click_values):
    return len(click_values[np.isnan(click_values)])


print(get_negative_values_number(orders))
print(get_nan_values_number(orders))
