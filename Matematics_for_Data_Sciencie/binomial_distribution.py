import numpy as np
from numpy.random import binomial
#from scipy.stats import binom
from math import factorial
#import matplotlib.pyplot as plt

def plot_hist(num_trials): #Función para realizar el experimento aleatorio, debemos implementar las librerias. 
  arr = []
  for _ in range(num_trials):
    arr.append(binomial(3, 0.5))
  distribucion_simulada = np.unique(arr, return_counts=True)[1]/len(arr)
  distribucion_teorica = [binom(3, 0.5).pmf(k) for k in values]
  #plt.bar(values, distribucion_teorica, label = 'teoría', color = 'red')
  #plt.bar(values, distribucion_simulada, label = 'simulación', alpha = 0.5, color = 'blue')
  #plt.title('simulación con {} experimentos'.format(num_trials))
  #plt.show()



# definición de la distribución binomial 
def my_binomial(k, n, p):
  return factorial(n)/(factorial(k)*(factorial(n-k)))*pow(p,k)*pow(1-p, n-k)


if __name__ == "__main__":
    print(f'Funcition binomial {my_binomial(2, 3, 0.5)}')