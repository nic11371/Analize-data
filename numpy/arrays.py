import numpy as np


click_numbers = [5, 7, 12, 3]


def create_click_numbers_ndarray(click_numbers):
    return np.array(click_numbers)


def get_mean(click_mean):
    return np.ndarray.mean(click_mean)


def get_max_clicks_day(click):
    return np.ndarray.argmax(click) + 1


def get_min_clicks_day(click_day):
    return np.ndarray.argmin(click_day) + 1


delta = create_click_numbers_ndarray(click_numbers).max() \
    - create_click_numbers_ndarray(click_numbers).min()
ndarray = create_click_numbers_ndarray(click_numbers)
print(create_click_numbers_ndarray(click_numbers))
print(delta)
print(get_mean(ndarray))
print(get_max_clicks_day(ndarray))
print(get_min_clicks_day(ndarray))
