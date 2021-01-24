"""Funtion for calculate Media (Average) and the mediana (median)"""

#We need to do it more efficient 
import math 
import statistics
import numpy as np 
import scipy.stats  

def average(X): #Promedio 
    averag = sum(X)/len(X)
    return averag

def mediana(X): #Mediana 
    sorted_List = sorted(X) #Sorted (Ordenar) the measuremens
    print(sorted_List)
    List_Len = len(X)
    index = (List_Len - 1)//2
    
    if (List_Len % 2):
        return sorted_List[index]
    else:
        return (sorted_List[index] + sorted_List[index + 1]) / 2

def variance(X): #Varianza 
    mu = average(X)
    accumulator = 0
    for x in X:
        accumulator += (x - mu)**2
    return  accumulator / size(X)

def standard_deviation(X): #Desviasción estandar 
    return variance(X)**0.5


def average_recort(X):  #Media recortada
    liminf = scipy.stats.scoreatpercentile(X,20)
    limsup = scipy.stats.scoreatpercentile(X,80)        #Ordenamos el conjunto de datos de menor a mayor 
    print(f'Limite Inferior {liminf} Limite superior {limsup}')
    trimean = scipy.stats.mstats.tmean(X,(2.8,5.4))
    print(f'The recort average is {trimean}')
    #trimean = scipy.stats.mstats.tmean(X,(108.2,136.025)    #Necesitamos tomar los datos dependiendo del porcentaje que vamos a eliminar 
        #Otra alternativa es eliminar los datos extremos

def size(X): #tamaño de la muestra 
    return len(X)


if __name__ == "__main__":
    X = [3.4, 2.5, 4.8, 2.9, 3.6, 2.8, 3.3, 5.6, 3.7, 2.8, 4.4, 4.0, 5.2, 3.0, 4.8]
    print(X)
    average_recort(X)
    mediana(X)
    #print(f'The average is: {average(X)}')
    #print(f'The median is: {mediana(X)}')
    #print(f'The average recort is {average_recort(X)}')
    #print(f'The variance is: {variance(X)}')
