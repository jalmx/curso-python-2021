autos = {
    'carro1' : 'vochito',
    'carro2' : 'jetta',
    'camion1' : 'volteo',
    'camion2' : 'trailer',
    'lengt'  :  4,
    'editable': True
}

camiones = {} # diccionario vacio
camionetas = dict() # diccionario vacio

print(autos['lengt'])
print(autos['carro1'])
print(autos['editable'])

print(autos.get('hola'))

camiones['camion1'] = "trailer" # agregando
camiones['camion2'] = "volteo"

print(camiones)

camiones['camion1'] = "camioncito"# modificando

print(camiones)

# crear un diccionario vacio
# agregar los siguientes elementos
# llave : valor
# golosina1 : sabrita
# golosina2 : coca
# golosina3 : gansito
# agregar 2 elementos mas, que tu quieras
# imprimir el diccionario

for key in autos:
    print(f'La llave {key} tiene el valor: {autos[key]}')

print('=====================')

for key in autos.keys():
    print(key)

print('=====================')

for valor in autos.values():
    print(valor)

print('=====================')

lista = list() # lista vacia
lista2 = []  # lista vacia

tupla = tuple() #tupla vacia
tupla2 = () # tupla vacia

dicc = dict() # diccionario vacio
dicc2 = {} # diccionario vacio

print('=================================')

numeros = [1,58,6,9,3,4,6,1,69,1,61,54]

indice, valor = (1, 25) # destructuracion
indice, valor, otro  = 25 , 65, 85 # multi asignacion

print(indice)
print(valor)
print(otro)

for indice, valor in enumerate(numeros):
    print(f'En el {indice} tiene el valor {valor}')

print('=======================================')

for index, key in enumerate(autos):
    print(f'En el {index} tiene el valor {key}')