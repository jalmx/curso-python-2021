carros = [ "vochito", "tsuru", 'jetta']

# recorrer los elementos de la lista
for carro in carros:
    print(carro)

print('==========================')
# agregar a la lista "camioneta"
carros.append("camioneta")

for carro in carros:
    print(carro)
print('==========================')
# eliminar el "tsuru" de la lista
carros.remove('tsuru')

for carro in carros:
    print(carro)

print('==========================')
# agregar 'volteo' al final de la lista
carros.insert(4, "volteo")

for carro in carros:
    print(carro)

print('==========================')
# agregar 'nissan' al principio de la lista
carros.insert(0, "nissan")

for carro in carros:
    print(carro)

print('==========================')

# obtener el indice del elemento 'vochito'
indice = carros.index('vochito')
print('El indice de vochito es:',indice)

print('==========================')
carros.sort() # ordena la lista y ya
print(carros)

print(sorted(carros)) # ordena la lista y la devuelve

print(len(carros))
print(len("hola"))

print('==========================')

del carros[4] # eliminar al elemento que esta en el indice 4

for carro in carros:
    print(carro)

print('==========================')