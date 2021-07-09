import math

redondeo_abajo = math.floor(4.23)
redondeo_arriba = math.ceil(1.23)

print(redondeo_abajo)
print(redondeo_arriba)

print("potencia")

print(3.2**2)
print(pow(3.2,2) )
print(math.pow(3.2,2))

print("raiz cuadrada")
numero = 25
print( math.sqrt(numero) )

print("=========")

print("Coseno de 30", math.cos(30))
print("Seno de 30", math.sin(30))
print("Tangente de 30", math.tan(30))


print("PI", math.pi)
print("Euler", math.e)

numeros = [2,1,5,6,8,1,96,5,41,91,8,51,6,1,51,6]

print("La suma es ", sum(numeros))

suma = 0

for v in numeros:
    suma += v

print(suma)