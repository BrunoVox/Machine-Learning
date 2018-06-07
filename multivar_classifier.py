import scipy.stats as sp

def multivar_density(x, mean, cov):
    return sp.multivariate_normal.pdf(x, mean, cov)