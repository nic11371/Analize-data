import numpy as np


def min_max_scaler(image_mnist):
    image = np.array(image_mnist)
    max_value = image.max()
    min_value = image.min()
    return image - min_value / max_value - min_value
