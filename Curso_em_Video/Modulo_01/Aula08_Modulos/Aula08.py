# Importação de bibliotecas

import math
#ceil arredonda o némero para cima
#floor arredonda o némero para baixo
#trunc irá eliminar qualquer numero apos a virgula

num = int(input('Digite um numero: '))
raiz = math.sqrt(num)
print('A raiz de um {} é igual a {}'.format(num, math.ceil(raiz)))

#___________________________________________________________________

import random #imprime um número aleatorio entre 0 e 1
num = random.randint(1, 10)
print(num)