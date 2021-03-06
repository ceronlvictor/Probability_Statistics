"""Se realiza un estudio acerca de los efectos del tabaquismo sobre 
los patrones de sueño. La medición que se observa es el tiempo, en 
minutos,  que toma quedar dormido se obtienen los siguientes datos:

    Fumadores 
            69.3, 56.0, 22.1, 47.6, 53.2, 48.1, 52.7, 34.4, 60.2, 43.8, 23.2, 13.8 
    
    No fumadores 

    28.6, 25.1, 26.4, 34.9, 29.8, 28.4, 38.5, 30.2, 30.6, 31.8, 41.6, 21.1, 36.0, 37.9, 13.9 
    
    a)	Calcule la media de la muestra para cada grupo
    b)	Calcule la desviación estándar de la muestra para cada grupo 
    c)	Elabore una gráfica de puntos de los conjuntos de datos AYB 
        en la misma línea 
    d)	Comente qué clase de efecto parece tener el hecho de fumar sobre 
        el tiempo que se requiere para quedarse dormido """

from location_measures import average, standard_deviation

if __name__=='__main__':
    smoking_group = [69.3, 56.0, 22.1, 47.6, 53.2, 48.1, 52.7, 34.4, 60.2, 43.8, 23.2, 13.8]
    not_smoking_group = [28.6, 25.1, 26.4, 34.9, 29.8, 28.4, 38.5, 30.2, 30.6, 31.8, 41.6, 21.1, 36.0, 37.9, 13.9]
    print(f'The average of the smoking group is: {average(smoking_group)}')
    print(f'The standard deviation of the smoking group is: {standard_deviation(smoking_group)}')
    print(f'\n The average of the smoking group is: {average(not_smoking_group)}')
    print(f'The standard deviation of the smoking group is: {standard_deviation(not_smoking_group)}')
    print('\nParece que el efecto de fumar afecta notablemente al timepo de quedar dormido debido a \nque el promedio del grupo así lo muestra al ser mas grande.')