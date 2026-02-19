'''
Exercício 78: Maior e Menor Valores na Lista
O que fazer: Faça um programa que leia 5 valores numéricos e guarde-os numa lista. No final, mostre qual foi o maior e o menor valor digitado e as suas respetivas posições na lista.
'''

valores = []
for i in range(1, 6):
    valores.append(int(input(f'Digite o {i}° valor: ')))

print(f'Os valores digitados: {valores}')
print(f'O maior valor é: {max(valores)}')
print(f'O menor valor é: {min(valores)}')