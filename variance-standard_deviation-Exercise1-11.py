"""Considera los datos del ejercicio 1.5 de la página 13. Calcule 
la varianza de la muestra y la desviación estándar de la muestra 
para ambos grupos el de tratamiento y el de control.
    a)Varianza
    b)Desviación estandar """

from location_measures import variance, standard_deviation

if __name__ == "__main__":
    control_group = [7, 3, -4, 14, 2, 5, 22, -7, 9, 5]
    treatment_group = [-6, 5, 9, 4, 4, 12, 37, 5, 3, 3]
    print(f'The variance of the control group is: {variance(control_group)}')
    print(f'The standard deviation of the control group is: {standard_deviation(control_group)}')
    print('\n')
    print(f'The variance of the treatment group is: {variance(treatment_group)}')
    print(f'The standard deviation of the treatment group is: {standard_deviation(treatment_group)}')

