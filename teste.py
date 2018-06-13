import random
import numpy as np

a = [1, 2, 3, 4, 5, 6, 7, 8, 9]

b = [0, 0, 0, 0, 0, 0, 0, 0, 0]

print(np.correlate(a, b))