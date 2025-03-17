import numpy as np


def mnist_data_converter(image_mnist):
    image = np.array(image_mnist)
    length = np.sqrt(image.shape)
    image = image.reshape(length, length)
    return image
