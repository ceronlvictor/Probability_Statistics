"""Veinte hombres adultos de entre 30 y 40 años de edad participaron en 
un estudio para evaluar el efecto de cierto régimen de salud, qué incluye dieta 
y ejercicio, en el colesterol sanguíneo. Se eligieron aleatoriamente diez para 
el grupo de control y los otros diez se asignaron para participar en el régimen 
como el grupo de tratamiento durante un periodo de 6 meses. 

    a) Elabore una gráfica de puntos con los datos de ambos grupos en la misma gráfica
    b) Calcule la media la mediana y la media recortada al 10% para ambos grupos 
    c) explícame porque la diferencia en las medidas sugiere una conclusión acerca del 
    efecto de régimen en tanto que la diferencia en las medianas o las medias recordadas 
    requiere una conclusión diferente """
from location_measures import average, mediana, size

if __name__ == '__main__':
    control_group = [7, 3, -4, 14, 2, 5, 22, -7, 9, 5]
    treatment_group = [-6, 5, 9, 4, 4, 12, 37, 5, 3, 3]
    print('\n')
    print(f'The measuraments of the control group are: {control_group}')
    print(f'The size of the control group is: {size(control_group)}')
    print(f'The average of the control gruop is: {average(control_group)}')
    print(f'The median of the control group is: {mediana(control_group)}')
    print('\n')
    print('*' * 70)
    print('\n')
    print(f'The measuraments of the treatment group are: {treatment_group}')
    print(f'The size of the the treatment group is: {size(treatment_group)}')
    print(f'The average of the treatment gruop is: {average(treatment_group)}')
    print(f'The median of the treatment group is: {mediana(treatment_group)}')
    print('\n')