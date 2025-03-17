import numpy as np


clicks = np.array([[4, 2], [3, 1], [2, 2], [4, 8], [5, 3], [4, 0], [6, 2]])
clicks_2 = np.array([
    [319, 265, 319, 328],
    [292, 274, 292, 301],
    [283, 301, 274, 283],
    [328, 364, 328, 319],
    [391, 355, 373, 337],
    [445, 418, 409, 445],
    [481, 400, 481, 409],
    [333, 267, 333, 344],
    [300, 278, 300, 311],
    [289, 311, 278, 289],
    [344, 388, 344, 333],
    [421, 377, 399, 355],
    [487, 454, 443, 487],
    [531, 432, 531, 443],
    [312, 264, 312, 320],
    [288, 272, 288, 296],
    [280, 296, 272, 280],
    [320, 352, 320, 312],
    [376, 344, 360, 328],
    [424, 400, 392, 424],
    [456, 384, 456, 392],
    [347, 269, 347, 360],
    [308, 282, 308, 321],
    [295, 321, 282, 295],
    [360, 412, 360, 347],
    [451, 399, 425, 373],
    [529, 490, 477, 529],
    [581, 464, 581, 477],
    ]
)


def get_max_weekly(click):
    weeks_count = len(clicks) // 7
    return [click[week * 7: week * 7 + 7].max() for week in range(weeks_count)]


def get_min_weekly(click):
    weeks_count = len(clicks) // 7
    return [click[week * 7: week * 7 + 7].min() for week in range(weeks_count)]


def get_day_of_week_mean(click):
    return [click[week::7].mean() for week in range(7)]


def get_placement_max_clicks(click, num):
    return click[:, num].max()


print(get_max_weekly(clicks_2))
print(get_min_weekly(clicks_2))
print(get_day_of_week_mean(clicks))
print(get_placement_max_clicks(clicks, 0))
print(get_placement_max_clicks(clicks, 1))
