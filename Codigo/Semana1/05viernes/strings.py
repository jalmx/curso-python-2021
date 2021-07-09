mensaje = "    hola como estas, ME GUSTA MUCHO PROGRAMAR, programar es lo hoy   "

# quitarle los espacios
# normalizar texto
# buscar la palabra programacion

print(mensaje)
mensaje = mensaje.strip()
print(mensaje)
mensaje = mensaje.capitalize()
print(mensaje)

print(mensaje.find('programar'))
print(mensaje.index('programar'))
print(mensaje.count('programar'))

print(mensaje.split(","))
print(len(mensaje.split(",")))