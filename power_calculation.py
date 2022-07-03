import numpy as np
from scipy import stats

def icdf(x):
    return(stats.norm.ppf(x))
icdf(0.8)

def power(delta, sigma, alpha, pi):
    result = (icdf(1-alpha)-icdf(1-pi))**2 * 2 * sigma**2/delta**2
    return(result)

power(delta= 200, sigma=2815, alpha=0.1, pi=0.8)