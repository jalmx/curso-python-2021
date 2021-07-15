# calcule la potencia de un numero, pero la potencia es opcional, por
# default el valor lo eleva al cuadrado

# calcule la fuerza, parametros que recibe son masa y aceleracion,
# pero si no me la aceleracion, por default es el valor de la gravedad

def potencia(base, exp=2):
    return base ** exp

def fuerza(masa, aceleracion=9.81):
    return masa * aceleracion

print(potencia(2))
print(potencia(3,3))

print(fuerza(1))
print(fuerza(5, 8.36))