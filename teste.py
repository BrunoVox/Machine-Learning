import random
import numpy as np

a = np.matrix([[1,1],[1,1]])
b = np.matrix([[1,1],[1,2]])

if a.all() == b.all():
    print("ok")
