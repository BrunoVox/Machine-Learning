import random
import numpy as np

a = np.matrix([1,1,1,1])
b = np.matrix([1,1,1,2])

c = []

c.append(a)
c.append(b)
print((c[1])[0, 3])