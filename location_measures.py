"""Funtion for calculate Media (Average) and the mediana (median)"""
import math 
import statistics

def average(X):
    averag = sum(X)/len(X)
    return averag

def mediana(X):
    sorted_List = sorted(X) #Sorted (Ordenar) the measuremens
    List_Len = len(X)
    index = (List_Len - 1)//2
    
    if (List_Len % 2):
        return sorted_List[index]
    else:
        return (sorted_List[index] + sorted_List[index + 1]) / 2

def variance(X):
    n = len(X) 
    average = sum(X)/n
    suma = [(x - n)**2 for x in X]
    sigma  = sum(suma) / n 
    return  sigma

def standard_deviation(X):
    n = len(X) 
    average = sum(X)/n
    suma = [(x - n)**2 for x in X]
    sigma  = sum(suma) / n 
    standard_dev = sigma ** 0.5
    return standard_dev


def average_recort(X):
    X = sorted (X) #Ordenamos el conjunto de datos de menor a mayor 
    #Necesitamos tomar los datos dependiendo del porcentaje que vamos a eliminar 
    #Otra alternativa es eliminar los datos extremos
    return X

def size(X):
    return len(X)


if __name__ == "__main__":
    X = [3.4, 2.5, 4.8, 2.9, 3.6, 2.8, 3.3, 5.6, 3.7, 2.8, 4.4, 4.0, 5.2, 3.0, 4.8]
    print(X)
    print(f'The average is: {average(X)}')
    print(f'The median is: {mediana(X)}')
    print(f'THe average recort is {average_recort(X)}')
    average(X)
    mediana(X)
    average_recort(X)