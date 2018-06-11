import random
import numpy as np

a = np.matrix([[1,1],[1,1]])
b = np.matrix([[1,1],[1,2]])
c = np.zeros(7,).tolist()
c[0] = a[0].tolist()
print(c)