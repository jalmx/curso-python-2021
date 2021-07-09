#_-encoding:utf8-_
#solicitar al usuario 10 números e indicar si es par o impar

contador = 1

while contador <=10:
    valor = int(input("Dar el valor {}: ".format(contador)))

    if not(valor % 2):
        print("El numero que me diste es PAR")
    else:
        print("El numero que me diste es IMPAR")

    contador += 1  
print("Continua el programa")