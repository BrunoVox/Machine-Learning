import random
import numpy as np

a = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]


# with open("out.txt", "w") as f:
#     for line in a:
#         np.savetxt(f, line, fmt="%.2f")

np.savetxt("out.txt", a, delimiter=",", fmt="%.2f")