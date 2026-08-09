'''
Exercício 83: Validando Expressões Matemáticas
O que fazer: Crie um programa onde o utilizador digite uma expressão qualquer que use parênteses. O teu aplicativo deverá analisar se a expressão passada está com os parênteses abertos e fechados na ordem correta.
'''

expressao = str(input('Digite a expressão: '))
pilha = []
for simb in expressao:
    if simb == '(':
        pilha.append('(')
    elif simb == ')':
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(')')
            break

if len(pilha) == 0:
    print('Sua expressão está valida!')
else:
    print('Sua expressão está errada!')