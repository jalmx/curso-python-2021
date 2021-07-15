def suma(x, y):
    resultado = x + y
    return resultado


def area_circulo(radio, pi=3.1415931265165):
    return pi * radio **2

def mensaje(texto="hola", sep=',', lower=True):
    texto = texto.replace(" ", sep)

    if not lower: 
        texto = texto.upper()
    print(texto)


print( suma(6, 9) )

print(f'El area del circulo es { area_circulo(7) }')

area_c = area_circulo(pi=3.15, radio=5)
print(f'El area del circulo es { area_c}')

print("Estoy en un print", "otro string",sep='+',end='\t\n')

mensaje(lower=False)
mensaje(sep='/', texto="como estas ???")
