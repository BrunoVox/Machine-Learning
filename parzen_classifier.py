# from scipy.stats import gaussian_kde
import numpy as np
# from scipy.stats import kde
# from sklearn.neighbors import KernelDensity as kd
from matrix import complete_view, shape_view, rgb_view

# n = len(complete_view[:])
# print(kd(kernel="gaussian", bandwidth=0.2).fit(complete_view))

def parzen_window(x, xi, h):
    amostra = (x - xi) / h
    pwf = (2 * np.pi) ** (- 1 / 2) * np.exp(-(0.5) * (amostra ** 2))
    return pwf

def parzen_density(pwf_product, h):
    p = (1 / (210 * (h ** 18))) * pwf_product
    return p

# h = np.array([0.2, 0.6, 1, 1.4, 1.8])