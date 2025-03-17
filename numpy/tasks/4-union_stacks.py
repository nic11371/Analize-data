import numpy as np


TEXT = ['мыла', 'мама', 'мама', 'раму', 'мыла', 'мама']


def text2vec(text):
    code_rules = {
        'мама': (0, 2, 1),
        'мыла': (1, 3, 0),
        'раму': (1, 1, 2),
    }
    return np.hstack([np.array(code_rules[word]) for word in text])


def text2matrix(text):
    code_rules = {
        'мама': (0, 2, 1),
        'мыла': (1, 3, 0),
        'раму': (1, 1, 2),
    }
    return np.vstack([np.array(code_rules[word]) for word in text])


print(text2vec(TEXT))
print(text2matrix(TEXT))
# END
