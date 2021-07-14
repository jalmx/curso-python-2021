from random import choice as elemetet_random
from random import randint as numero_random

saludos = ['Hola, como estas', "Hello", " Bienvenido",'Hola']
hobbies = ['leer', 'correr', 'dormir' ]
nombres = ['BotPy','PatitoBot', 'UnicornioBot']

print(elemetet_random(saludos))
nombre = input('Como te llamas? ')

nombres.append(nombre)

print('Me llamo ' + elemetet_random(nombres))

print("Que bonito nombre tienes, tengo otro amigo que se llama " + elemetet_random(nombres))

edad = int(input('Que edad tienes? '))

print("Orale!!! Yo tengo " + str((edad + numero_random(0,10))))

hobby = input("Que es lo que te gusta hacer? ")
hobbies.append(hobby)

print("que buena onda, a mi me gusta " + elemetet_random(hobbies))

respuesta = input("Quieres ser mi amigo?!!")

if respuesta.lower().strip() == 'si':
    print("Seremos los mejores amigos!!!! Wiiiii!!!!")
else:
    print("A mi nadie me desprecia!!! Te vere en tus peores pesadillas!!! >:)")
