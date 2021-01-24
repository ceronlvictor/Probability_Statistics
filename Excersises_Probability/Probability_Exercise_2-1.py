"""Liste los elementos de cada uno de los siguientes espacios muestrales
    a)Conjunto de numeros enteros entre  1 y 50 que son divisibles entre 8
    b) El conjunto S = {x|x**2 + 4x -5 = 0}
    c) EL conjunto de resultados cuando se lanza una moneda al aire hasta 
    que aparecen una cruz o tres caras
    d) El conjunto de S = {x | x es un continente}
    e) El conjunto de S = {x | 2x -4 >= 0 y x < 1}"""

def main():
    s_a = []
    x = 0
    x_b = -200
    while x < 51:
        x+=1
        if x % 8 == 0:
            s_a.append(x)
    print(f'The elements of the sample space of the a) are: {s_a}')

    while x_b < 200:
        x_b += 1
        if x_b**2 + 4*x_b -5 == 0:
            print(x_b)

    


if __name__ == '__main__':
    main()


