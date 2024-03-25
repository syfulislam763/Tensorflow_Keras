import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'
import tensorflow as tf
import math
import numpy as np


a = np.array([
        [3, 4, 5],
        [1, 2, 3],
        [6, 7, 8]
    ])

b = a*5
print(b)
