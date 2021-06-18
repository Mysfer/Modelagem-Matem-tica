from matrizes import Matrizes
import numpy as np
from numpy.core.fromnumeric import transpose
from tomografia import Tomografia

t = Tomografia()

a = np.array([
    [[0], [0], [0], [0], [0], [0], [1], [1], [1]],
    [[0], [0], [0], [1], [1], [1], [0], [0], [0]],
    [[1], [1], [1], [0], [0], [0], [0], [0], [0]],
    [[0], [0], [0], [0], [0], [1], [0], [1], [1]],
    [[0], [0], [1], [0], [1], [0], [1], [0], [0]],
    [[1], [1], [0], [1], [0], [0], [0], [0], [0]],
    [[0], [0], [1], [0], [0], [1], [0], [0], [1]],
    [[0], [1], [0], [0], [1], [0], [0], [1], [0]],
    [[1], [0], [0], [1], [0], [0], [1], [0], [0]],
    [[0], [1], [1], [0], [0], [1], [0], [0], [0]],
    [[1], [0], [0], [0], [1], [0], [0], [0], [1]],
    [[0], [0], [0], [1], [0], [0], [1], [1], [0]]
])

b = np.array([
    13,
    15,
    8,
    14.79,
    14.31,
    3.81,
    18,
    12,
    6,
    10.51,
    16.13,
    7.04
])

x = t.densidade(a, b)
print(x)