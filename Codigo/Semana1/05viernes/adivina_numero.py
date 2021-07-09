import random

numero_random = random.randrange(20)

print("Vamos a jugar xD")

intento = 0
while True:
    if intento >= 3:
        print("Lastima margarito :( ")
        print("El numero era:", numero_random )
        break

    numero_usuario = int(input("Adivina el numero, dime : "))

    if numero_usuario > numero_random:
        print("Es MENOR")
        intento +=1
    elif numero_usuario < numero_random:
        print("Es MAYOR")
        intento +=1
    elif numero_random == numero_usuario:
        print("Felicidades!!! Ganaste!!!!! \\o/")
        break
    

