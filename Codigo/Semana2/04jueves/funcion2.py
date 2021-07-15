def area_circulo(radio, pi=3.14):
    print(f'El area del circulo es { pi * radio**2 }')

area_circulo(5)
area_circulo(5, 3.1415921256165165)

def area_rectangulos(b, h=0):
    if not h :
        h = b
    print(f'El area del rentangulo es {b*h}')


area_rectangulos(5)
area_rectangulos(5,3)