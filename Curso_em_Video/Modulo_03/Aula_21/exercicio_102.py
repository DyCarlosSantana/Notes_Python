# Este é o arquivo número 102
"""
Função para Fatorial

O que fazer: Crie um programa que tenha uma função fatorial(), que receba dois parâmetros: o primeiro que indique o número a calcular e o outro chamado show, que será um valor lógico (opcional) indicando se será mostrado ou não no ecrã o processo de cálculo do fatorial.
"""
def fatorial(num, show=False):
    f = 1
    for c in range(num, 0, -1):
        f  *= c
        if show:
            print(f'{c}', end=' ')
            if c > 1:
                print(f'x', end=' ')
            else:
                print(f'=', end=' ')
    return f


print(fatorial(5, show=True))