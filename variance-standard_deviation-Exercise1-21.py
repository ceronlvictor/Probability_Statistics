"""La duración de fallas eléctricas en minutos se presenta en la siguiente tabla 

22 18 135 15 90 78 69 98 102 83 55 28 121 120 13 22 124 112 70 66 74 89 103 24 21 112 21 40 98 87 132 115 21 28 43 37 50 96 118 158 74 78 83 95 

    a) Calcula la media y la mediana muestral es de las duraciones de la falla eléctrica 
    b) Calcula la desviación estándar de las duraciones de la falla eléctrica""" 
from location_measures import average, variance, mediana, standard_deviation

if __name__=="__main__":
    electric_faults = [22, 18, 135, 15, 90, 78, 69, 98, 102, 83, 55, 28, 121, 120, 13, 22, 124, 112, 70, 66, 74, 89, 103, 24, 21, 112, 21, 40, 98, 87, 132, 115, 21, 28, 43, 37, 50, 96, 118, 158, 74, 78, 83, 95]
    print(f'\nThe sample mean is: {average(electric_faults)}')
    print(f'The sample median is: {mediana(electric_faults)}')
    print(f'The sample variance is: {variance(electric_faults)}')
    print(f'THe standard deviation is: {standard_deviation(electric_faults)}')
