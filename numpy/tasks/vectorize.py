import numpy as np


clicks = [[5, 7], [12, 3]]


def get_even_clicks(click):
    if click % 2 != 0:
        click += 1
    return click


get_even_clicks = np.vectorize(get_even_clicks)


print(get_even_clicks(clicks))
