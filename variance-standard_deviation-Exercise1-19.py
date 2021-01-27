"""Los siguientes datos representan la duración de vida en años medida 
al entero más cercano de 30 bombas de combustible similares.

2.0 3.0 0.3 3.3 1.3 0.4 0.2  6.0 5.5 6.5 0.2 2.3 1.5 4.0 5.9 1.8 4.7 0.7 4.5 0.3 1.5 0.5 2.5 5.0 1.0 6.0 5.6 6.0 1.2 0.2  

    b) Construya un diagrama de tallo y hojas para la vida en años de las 
        bombas de combustible utilizando el dígito a la izquierda del punto 
        decimal como el tallo para cada observación determina una distribución 
        de frecuencias relativas 
        
    a) Calcula la media el rango y la desviación estándar de lo nuestra """

from location_measures import average, size, standard_deviation


if __name__=="__main__":
    time_life = [2.0, 3.0, 0.3, 3.3, 1.3, 0.4, 0.2,  6.0, 5.5, 6.5, 0.2, 2.3, 1.5, 4.0, 5.9, 1.8, 4.7, 0.7, 4.5, 0.3, 1.5, 0.5, 2.5, 5.0, 1.0, 6.0, 5.6, 6.0, 1.2, 0.2]
    print(f'The sample mean is: {average(time_life)}')
    print(f'The range of the sample is: {size(time_life)}')
    print(f'The standard deviation is: {standard_deviation(time_life)}')
