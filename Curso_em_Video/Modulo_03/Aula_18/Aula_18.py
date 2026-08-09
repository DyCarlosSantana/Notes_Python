"""
teste = []
teste.append('Carlos')
teste.append(22)

galera = []
galera.append(teste[:])
teste[0] = 'Bruna'
teste[1] = 14
galera.append(teste[:])
print(galera)
"""

# galera =[["João", 10], ["Maria", 15], ["Gustavo", 20], ["Livia", 30]]

# print(galera[0][0])
# print(galera[2][0])
# print(galera[-1][1])

"""
for pessoa in galera:
    print(f"{pessoa[0]} tem {pessoa[1]} anos de idade")
"""
galera = []
dados = []
total_maior = total_menor = 0

for i in range(0, 3):
    dados.append(str(input("Nome: ")))
    dados.append(int(input("Idade: ")))
    galera.append(dados[:])
    dados.clear()

print(galera)

for pessoa in galera:
    if pessoa[1] >= 18:
        print(f'{pessoa[0]} é maior de idade')
        total_maior += 1
    else:
        print(f'{pessoa[0]} é menor de idade')
        total_menor += 1

print(f"Temos {total_maior} maior(s) de idade e {total_menor} menor(s) de idade: ")

"""
Exercício 84: Lista Composta e Análise de Dados
O que fazer: Faça um programa que leia o nome e o peso de várias pessoas, guardando tudo numa lista composta. No final, mostre:
Quantas pessoas foram cadastradas.
Uma listagem com as pessoas mais pesadas (mostre o peso e os nomes).
Uma listagem com as pessoas mais leves (mostre o peso e os nomes).

Exercício 85: Listas com Pares e Ímpares
O que fazer: Crie um programa onde o utilizador possa digitar sete valores numéricos e registe-os numa única lista que mantenha separados os valores pares e ímpares. No final, mostre os valores pares e ímpares em ordem crescente.
Dica do Cleitin: Vais precisar de uma lista que contém duas listas internas: [[pares], [ímpares]].

Exercício 86: Matriz em Python
O que fazer: Crie um programa que declare uma matriz de dimensão 3x3 e preencha com valores lidos pelo teclado. No final, mostre a matriz no ecrã, com a formatação correta.

Exercício 87: Mais sobre Matriz
O que fazer: Aprimore o desafio anterior, mostrando no final:
A soma de todos os valores pares digitados.
A soma dos valores da terceira coluna.
O maior valor da segunda linha.

Exercício 88: Palpites para a Mega Sena
O que fazer: Faça um programa que ajude um jogador da Mega Sena a criar palpites. O programa vai perguntar quantos jogos serão gerados e vai sortear 6 números entre 1 e 60 para cada jogo, registando tudo numa lista composta.

Exercício 89: Boletim com Listas Compostas
O que fazer: Crie um programa que leia nome e duas notas de vários alunos e guarde tudo numa lista composta. No final, mostre um boletim contendo a média de cada um e permita que o utilizador possa consultar as notas de cada aluno individualmente.
"""