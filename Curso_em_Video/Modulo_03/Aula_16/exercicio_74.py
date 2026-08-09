'''
    74 - Crie um programa que irá gerar 5 números aleatorios e colocar em uma tupla. Depois disso, mostre a listagem de números gerados e também indique o menor e o maior valor que estão na tupla
'''

from random import randint

numeros = (randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10))
print('Os valores sorteados foram:', end='')
for n in numeros:
    print(f' {n}, ', end='')

print(f'\nO maior numero sorteado foi: {max(numeros)}')
print(f'O menor numero sorteado foi: {min(numeros)}')
