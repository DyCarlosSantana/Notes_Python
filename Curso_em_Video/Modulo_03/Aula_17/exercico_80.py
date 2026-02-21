'''
Exercício 80: Lista Ordenada sem sort()
O que fazer: Crie um programa onde o utilizador possa digitar cinco valores numéricos e registe-os numa lista, já na posição correta de inserção (sem usar o sort()). No final, mostre a lista ordenada no ecrã.
Dica do Cleitin: Este é um exercício de lógica pura (algoritmo de ordenação manual).
'''
lista = []
for i in range(1, 6):
    n = int(input(f'Digite o {i}° número: '))
    if i == 0 or n > lista[len(lista)]: #ou [-1]
        lista.append(n)
    else:
        pos = 0
        while pos < len(lista):
            if n <= lista[pos]:
                lista.insert(pos, n)
                break
            pos += 1
print('---'*10)
print(lista)