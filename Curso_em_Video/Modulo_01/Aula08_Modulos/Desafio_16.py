#Crie um progrma que leia um número real qualquer pelo teclado e mostre na tela a sua porção intera.
#EX: Digite o némero 6,127 tem sua porção inteira: 6.

import math

num = float(input('Digite um número: '))
int = math.trunc(num)
print('O número {} tem sua parte inteira {}'. format(num, int))