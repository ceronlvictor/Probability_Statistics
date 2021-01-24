"""Para el ejercicio 1.6 de la página 13 calcula la desviación 
estándar muestral de la resistencia a la tensión para las muestras 
de forma separada para ambas temperaturas ¿parece que un incremento 
en la temperatura influye en la variabilidad de la resistencia a la 
tensión? explique por qué"""
from location_measures import variance, standard_deviation, size, average

if __name__ == "__main__":
    resist_twenty = [2.7, 2.14, 2.2, 2.03, 2.21, 2.03, 2.05, 2.18, 2.09, 2.14, 2.11, 2.02]
    resist_forty_five = [2.25, 2.15, 2.49, 2.03, 2.37, 2.05, 1.99, 2.42, 2.08, 2.42, 2.29, 2.01]
    print(f'The size of the measurements in twenty degree Celsius: {size(resist_twenty)}')
    print(f'The size of the measurements in forty five degree Celsius {size(resist_forty_five)}')
    print(f'The average is: {average(resist_twenty)}\n')
    print(f'The variance when the temperature is twenty degrees is: {variance(resist_twenty)}')
    print(f'The standard deviation when the temperature is twenty degrees is: {standard_deviation(resist_twenty)}')
    print(f'The average is: {average(resist_forty_five)}\n')
    print(f'The variance when the temperature is forty five degrees is: {variance(resist_forty_five)}')
    print(f'The standard deviation when the temperature is forty five degrees is: {standard_deviation(resist_forty_five)}') 
    print('\n El incremento en la temperatura no influye en la variabilidad de la resistencia')   
    print('\n Esto es porque ')   