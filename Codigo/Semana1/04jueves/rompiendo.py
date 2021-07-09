# Vamos a hacer un ciclo infinito el cual vamos a romper cuando una condicion se cumpla

count = 0

while "unicornio":
    count += 1
    print("unicornio")
    
    if count == 50:
        break
    if count % 2:
        continue
    print("ponny")
    print("Continua el codigo del while")

print("fuera del while")