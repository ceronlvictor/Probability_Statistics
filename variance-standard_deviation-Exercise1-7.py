"""Considere los datos del tiempo de secado del ejercicio 1.1 de la 
página 13 calcula la varianza de la muestra y la desviación estándar de la muestra.
    a) Varianza de la muestra 
    b) Desviación estandar de la muestra"""
from location_measures import variance, standard_deviation

if __name__ == "__main__":
    measures = [3.4, 2.5, 4.8, 2.9, 3.6, 2.8, 3.3, 5.6, 3.7, 2.8, 4.4, 4.0, 5.2, 3.0, 4.8]
    print(f'The variance is: {variance(measures)}')
    print(f'The standar deviation is: {standard_deviation(measures)}')

