# Este é o arquivo número 104
"""
Exercício 104: Validando Entrada de Dados

O que fazer: Crie um programa que tenha uma função chamada leiaInt(), que vai funcionar de forma semelhante à função input() do Python, mas que faça a validação para aceitar apenas um valor numérico inteiro.
Ex: n = leiaInt('Digite um número: ')
"""
def leiaInt(msg=''):
    while True:
        valor = str(input(msg))
        if valor.isnumeric():
            valor = int(valor)
            resul_valor = isinstance(valor, int)
            print(f'Você digitou o número {valor}')
            if resul_valor == True:
                break
        else:
            print('ERRO: Digite um número valido!')
    
leiaInt('Digite um número: ')