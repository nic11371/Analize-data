import numpy as np


clicks_values = [
    [319, 265, 319, 328],
    [292, 274, 292, 301],
    [283, 301, 274, 283],
    [194, 200, 255, 306],
    [150, 222, 259, 310],
    [198, 204, 299, 318],
    [190, 266, 288, 300],
    [319, 265, 319, 329],
    [292, 274, 350, 301],
    [283, 301, 274, 283],
    [194, 200, 255, 306],
    [150, 222, 259, 310],
    [198, 204, 299, 318],
    [190, 266, 288, 300],
    [319, 265, 319, 328],
    [292, 274, 292, 301],
    [283, 301, 400, 283],
    [194, 200, 255, 306],
    [150, 222, 259, 310],
    [198, 204, 299, 318],
    [190, 266, 288, 300],
    [319, 265, 319, 328],
    [292, 274, 292, 301],
    [283, 301, 274, 283],
    [194, 200, 255, 306],
    [150, 222, 259, 310],
    [198, 204, 777, 318],
    [190, 266, 288, 300],
]


def create_click_numbers_ndarray(input_click):
    return np.array(input_click)


clicks = create_click_numbers_ndarray(clicks_values)


def get_max_weekly(clicks):
    return [
        clicks[monday * 7: monday * 7 + 7].max()
        for monday in range(4)
    ]


def get_mean_monday(clicks):
    return clicks[::7].mean()


print(get_max_weekly(clicks))
print(get_mean_monday(clicks))
