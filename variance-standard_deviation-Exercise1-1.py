"""Mediciones para el tiempo de Secado en horas de una marca de pintura esmaltada
    a)Tamaño de la muestra
    b)Media
    c)Mediana 
    d)Grafica de los datos 
    e)Media Recortada al 20%
    f)Que representa mejor los datos Media muestral o Media Recortada """

from location_measures import average, mediana, average_recort
from bokeh.plotting import figure, output_file, show

def grafic(measure):
    output_file = ('variance-standard_deviation-Exercise1.1.html')
    fig = figure()
    
    x_vals = list(measure)
    y_vals = 0
    fig.dot(x_vals, y_vals, size = 20)
    show(fig)

def main(measure):
    return len(measure)

if __name__ == "__main__":
    measure = [3.4, 2.5, 4.8, 2.9, 3.6, 2.8, 3.3, 5.6, 3.7, 2.8, 4.4, 4.0, 5.2, 3.0, 4.8]

    print(f'The measuraments are: {measure}')
    #a)
    print(f'The size of the sample is: {main(measure)}')
    #b)
    print(f'The average is: {average(measure)}')
    #c
    print(f'The median is: {mediana(measure)}')
    #d
    grafic(measure)
    #e
    print(f"The media recort is: {average_recort(measure)}")
