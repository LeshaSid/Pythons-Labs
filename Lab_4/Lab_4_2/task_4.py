import numpy as np
from scipy import integrate
import scipy.integrate as spi

def f(x):
    return x/(np.sqrt(x**4 + 16))

def integrate_f(f, a, b):
    result, error = spi.quad(f, a, b)
    return result

print(f"∫ от 0 до √3 [x/√(x⁴ + 16)] dx = {integrate_f(f, 0, np.sqrt(3))}")