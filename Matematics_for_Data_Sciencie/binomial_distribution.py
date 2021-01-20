import numpy as np
from numpy.random import binomial
#from scipy.stats import binom
from math import factorial
#import matplotlib.pyplot as plt

# definición de la distribución binomial 
def my_binomial(k, n, p):
  return factorial(n)/(factorial(k)*(factorial(n-k)))*pow(p,k)*pow(1-p, n-k)


if __name__ == "__main__":
    print(f'Funcition binomial {my_binomial(2, 3, 0.5)}')