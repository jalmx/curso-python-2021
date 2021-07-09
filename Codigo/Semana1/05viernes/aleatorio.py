import random

x=0
while x < 10:
    numero = random.random()
    print(numero)
    x +=1

print('================')

x=0
while x < 10:
    numero = random.randrange(11)
    print(numero)
    x +=1

print('================')

x=0
while x < 10:
    numero = random.randint(5,15)
    print(numero)
    x +=1

print('================')

autos = ['jetta', 'vochito', 'sentra','chevy']

auto = random.choice(autos)

print(auto)