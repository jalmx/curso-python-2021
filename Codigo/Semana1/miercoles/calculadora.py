# Damos el menu y guardamos la opcion del usuario
print("Calcualdora super WOW")
print("1) Suma")
print("2) Resta")
print("3) Multiplicar")
print("4) Dividir")
print("5) Salir")
opcion = int(input())

if opcion == 1:
    print("====== SUMA =======")
    valor_1 = int(input("Dar valor 1: " ))
    valor_2 = int(input("Dar valor 2: " ))
    suma = valor_1 + valor_2
    print("La suma es: " + str(suma))
elif opcion == 2:
    print("====== RESTA =======")
    valor_1 = int(input("Dar valor 1: " ))
    valor_2 = int(input("Dar valor 2: " ))
    resta = valor_1 - valor_2
    print("La resta es: " + str(resta))
elif opcion == 3:
    print("====== MULTIPLICAR =======")
    valor_1 = int(input("Dar valor 1: " ))
    valor_2 = int(input("Dar valor 2: " ))
    multiplicar = valor_1 * valor_2
    print("La multiplicacion es: " + str(multiplicar))
elif opcion == 4:
    print("====== DIVIDIR =======")
    valor_1 = int(input("Dar valor 1: " ))
    valor_2 = int(input("Dar valor 2: " ))
    dividir = valor_1 - valor_2
    print("La divicion es: " + str(dividir))
elif opcion == 5:
    print("Saliendo...")
else:
    print('Esta opcion no existe')