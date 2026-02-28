"""
Exercício 86: Matriz em Python
O que fazer: Crie um programa que declare uma matriz de dimensão 3x3 e preencha com valores lidos pelo teclado. No final, mostre a matriz no ecrã, com a formatação correta.
"""
matriz = [[], [], []]

for n in range(0, 3):
    matriz[0].append(int(input(f"Digite um número para a posição {n}: ")))
for n in range(3, 6):
    matriz[1].append(int(input(f"Digite um número para a posição {n}: ")))
for n in range(6, 9):
    matriz[2].append(int(input(f"Digite um número para a posição {n}: ")))

print(f"{matriz[0]}\n{matriz[1]}\n{matriz[2]}")


