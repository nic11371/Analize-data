import numpy as np


def get_stat_values(click_values):
    array = np.array(click_values)
    array_mean = array.mean()
    array_std = array.std()
    array_median = np.median(array)
    return array_mean, array_std, array_median


def get_min_value_position(clicks_values):
    return np.unravel_index(np.argmin(clicks_values), clicks_values.shape)
