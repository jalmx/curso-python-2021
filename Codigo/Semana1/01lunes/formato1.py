def main():
    numero = 5
    animal1 = "Tortuga"
    animal2 = "Perritos"

    frase = 'Tengo {} mascotas, una {} y 4 {}'.format(numero,animal1,animal2 , 'gato')

    frase2 = 'Tengo {2} mascotas, una {0} y 4 {1}, es {3}'.format(animal1, animal2, numero, False)
    # 0        1        2       3

    print(frase2)

