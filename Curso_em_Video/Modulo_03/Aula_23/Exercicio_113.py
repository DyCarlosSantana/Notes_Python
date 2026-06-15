# Este é o arquivo número 113
"""
Exercício 113: Funções de Leitura Robustas
    O que fazer: Reescreva a função leiaInt() que fizemos no Exercício 104, incluindo agora a possibilidade da digitação de um número de tipo inválido. Aproveite e crie também uma função chamada leiaFloat() com a mesma funcionalidade.
    - Dica do Cleitin: Usa um loop while True e blocos try/except para lidar com ValueError e KeyboardInterrupt.
"""

def leiaInt(msg):
    while True:
        try:
            valor = int(input(msg))
        except ValueError:
            print(f'ERRO: Digite um número inteiro valido')
        except KeyboardInterrupt:
            print('O Usuario preferiu não digitar esse valor')
            return 0
        else:
            return valor #return finaliza o loop e a função automaticamente


def leiaFloat(msg):
    while True:
        try:
            valor = float(input(msg))
        except ValueError:
            print(f'ERRO: Digite um número real valido')
        except KeyboardInterrupt:
            print('O Usuario preferiu não digitar esse valor')
            return 0
        else:
            return valor #return finaliza o loop e a função automaticamente


i = leiaInt('Digite um número inteiro: ')
r = leiaFloat('Digite um número real: ')
print(f'O valor inteiro é {i} e o valor real é {r}')