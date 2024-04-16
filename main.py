import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'
import tensorflow as tf
import math
import numpy as np


physical_devices = tf.config.experimental.list_physical_devices()
print(physical_devices)
