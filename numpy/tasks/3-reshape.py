import numpy as np
import random

MIN = 120
MAX = 250
SEED = 42
sells_1 = [7, 6, 12, 5, 3, 3, 8, 11, 12, 9, 5, 7, 4, 3, 9, 10, 8, 6, 3, 15, 2]


def sells():
    random.seed(SEED)
    return [random.randint(MIN, MAX) for _ in range(4 * 7 * 10)]


sells_2 = sells()


def create_weekly_sells_table(sells):
    sells_array = np.array(sells)
    # size = sells_array.shape
    return sells_array.reshape((-1, 7, 10))


print(create_weekly_sells_table(sells_2))
