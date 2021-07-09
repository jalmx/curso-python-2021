#Imprimir la tabla del 8, que vaya desde el 1 al 10.

tabla = 8
contador = 1

while contador <= 10:
    multiplicacion = tabla * contador
    print("{} x {} = {}".format(tabla, contador, multiplicacion))
    contador += 1