""" Un fabricante de componentes electrónicos se interesa en determinar 
el tiempo de vida de cierto tipo de batería. Una muestra en horas de vida 
es como la siguiente 
        
            123, 116, 122, 110, 175, 126, 125, 111, 118, 117, 
    
    a)Calcule la media y la mediana de la muestra 
    
    b)Qué característica en este conjunto de datos es la responsable de 
        la diferencia sustancial entre ambas """

from location_measures import average, mediana

if __name__=='__main__':
    time_life = [123, 116, 122, 110, 175, 126, 125, 111, 118, 117]
    print(f'The sample is: {time_life}')
    print(f'The Average is: {average(time_life)}')
    print(f'The median is: {mediana(time_life)}')
    print(f'The diference is because the extreme values afect the average')