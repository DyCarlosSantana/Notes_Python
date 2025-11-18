#Faça um programa que leia um número qualquer e mostre o seu fatorial
#Exemplo: 5!= 5x4x3x2x1= 120.

#FORMA MAIS SIMPLES UTILIZANDO UM MODULO...
from math import factorial
n = int(input('Digite um número: '))
fatorial = factorial(n)
print(f'O fatorial de {n} é {fatorial}')

#USANO O WHILE
n = int(input('Digite um número: '))
c = n
f = 1
print(f'Calculando \n{n}! =', end='')
while c > 0:
    print(' {}'.format(c), end='')
    print(' x ' if c > 1 else ' = ', end='')
    f *= c
    c -= 1
print(f)

#USANO O FOR
n = int(input('Digite um número: '))
f = 1
print(f'Calculando \n{n}! =', end='')
for c in range(n, 0, -1):
    print(' {}'.format(c), end='')
    print(' x ' if c > 1 else ' = ', end='')
    f *= c
print(f)