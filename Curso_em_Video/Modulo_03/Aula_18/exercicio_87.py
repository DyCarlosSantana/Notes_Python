"""
Exercício 87: Mais sobre Matriz
O que fazer: Aprimore o desafio anterior, mostrando no final:
A soma de todos os valores pares digitados.
A soma dos valores da terceira coluna.
O maior valor da segunda linha.
"""

matriz = [[], [], []]

for n in range(0, 3):
    try:
        matriz[0].append(int(input(f"Digite um número para a posição {n}: ")))
    except:
        print("Dado invalido! Tente novamente...")
for n in range(3, 6):
    try:
        matriz[1].append(int(input(f"Digite um número para a posição {n}: ")))
    except:
        print("Dado invalido! Tente novamente...")
for n in range(6, 9):
    try:
        matriz[2].append(int(input(f"Digite um número para a posição {n}: ")))
    except:
        print("Dado invalido! Tente novamente...")

print(f"{matriz[0]}\n{matriz[1]}\n{matriz[2]}")

pares = []
for lista in matriz:
    for n in lista:
        if n % 2 == 0:
            pares.append(n)
print(f"A soma de todos os valores pares é: {sum(pares)}")

colum3 = []
for lista in matriz:
    colum3.append(lista[1])
print(f"A soma dos valores da terceira coluna é: {sum(colum3)}")

maior = max(matriz[1])
print(f"O maior valor da segunda linha é : {maior}")

#Utilização do metodo sum para agilizar a somatoria