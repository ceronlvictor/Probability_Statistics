"""Funtion for calculate Media (Average) and the mediana (median)"""
import math 
import statistics

def average(X):
    return sum(X)/len(X)

def mediana(X):
    sorted_List = sorted(X) #Sorted (Ordenar) the measuremens
    List_Len = len(X)
    index = (List_Len - 1)//2
    
    if (List_Len % 2):
        return sorted_List[index]
    else:
        return (sorted_List[index] + sorted_List[index + 1]) / 2

def average_recort(X):
    sorted_List = sorted(X)

    for _ in X:
        quantity  = len(sorted_List)
        if quantity == 15:
            sorted_List.pop(0)
        if quantity == 14:
            sorted_List.pop(1)
        if quantity == 13:
            sorted_List.pop(2)
    return sum(X)/len(X)



if __name__ == "__main__":
    X = [3.4, 2.5, 4.8, 2.9, 3.6, 2.8, 3.3, 5.6, 3.7, 2.8, 4.4, 4.0, 5.2, 3.0, 4.8]
    print(f'The average is: {average(X)}')
    print(f'The median is: {mediana(X)}')
    print(f'THe average recort is {average_recort(X)}')
    average(X)
    mediana(X)
    average_recort(X)