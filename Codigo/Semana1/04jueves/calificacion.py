# Realizar una calculadora para sumar y restar, pero hasta que el usuario de la opcion de salir el programa terminará

opcion = 1

while opcion != 0:
    print("1)Suma")
    print("2)Resta")
    print("3)Salir")
    opcion = int(input())

    if opcion == 1:
        valor1 = float(input("Dar el primer valor: "))
        valor2 = float(input("Dar el segundo valor: "))
        resultado = valor1 + valor2
        print("La suma es " + resultado)
    elif opcion == 2:
        valor1 = float(input("Dar el primer valor: "))
        valor2 = float(input("Dar el segundo valor: "))
        resultado = valor1 - valor2
        print("La resta es " + resultado)
    elif opcion == 3:
        opcion = 0
    else:
        print("No existe esa opcion")

print("El programa termina")