import numpy as np


images = [0, 1, 2, 4, 8]


def standard_scaler(img):
    image = np.array(img)
    image_mean = image.mean()
    image_std = image.std()
    return (image - image_mean) / image_std


print(standard_scaler(images))
