# Este é o arquivo número 99
'''
Exercício 99: Função que descobre o maior
O que fazer: Faça um programa que tenha uma função chamada maior(), que receba vários parâmetros com valores inteiros. O teu programa tem de analisar todos os valores e dizer qual deles é o maior.
'''

def maior(*num):
    maior = 0
    for n in num:
        if n > maior:
            maior = n
    print('Analisando valores repassados...')
    print(f'-> {num} \nForma encontrados {len(num)} valores ao todo')
    print(f'O maior valor encontrado é {maior}')

maior(1, 4, 2, 6, 8, 3)