"""
Exercício 85: Listas com Pares e Ímpares
O que fazer: Crie um programa onde o utilizador possa digitar sete valores numéricos e registe-os numa única lista que mantenha separados os valores pares e ímpares. No final, mostre os valores pares e ímpares em ordem crescente.
Dica do Cleitin: Vais precisar de uma lista que contém duas listas internas: [[pares], [ímpares]].
"""
lista_numeros = [[], []]

for n in range(1, 8):
    valor = int(input(f"Digite o {n}° número: "))
    if valor % 2 == 0:
        lista_numeros[0].append(valor)
    else:
        lista_numeros[1].append(valor)

print(f"Lista completa: {lista_numeros}")
lista_numeros[0].sort()
lista_numeros[1].sort()
print(f"Números Pares: {lista_numeros[0]}")
print(f"Números Impares: {lista_numeros[1]}")