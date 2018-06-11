import random
import numpy as np

<<<<<<< HEAD
a = np.matrix([1,1,1,1])
b = np.matrix([1,1,1,2])

c = []

c.append(a)
c.append(b)
print((c[1])[0, 3])
=======
a = np.matrix([[1,1],[1,1]])
b = np.matrix([[1,1],[1,2]])
c = np.zeros(7,).tolist()
c[0] = a[0].tolist()
print(c)
>>>>>>> 618ea77940f3b84ca6e87fa9afa15be287d8b81f
