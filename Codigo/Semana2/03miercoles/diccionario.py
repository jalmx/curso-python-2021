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