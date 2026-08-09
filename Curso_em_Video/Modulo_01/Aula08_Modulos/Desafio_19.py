# Um professor quer sortear  um dos seus 4 alunos para pagar o quadro. Faça um programa que ajude ele, lendo o nome deles e sorteando um dos alunos.

import random

a1 = str(input('Digite o nome do aluno: '))
a2 = str(input('Digite o nome do aluno: '))
a3 = str(input('Digite o nome do aluno: '))
a4 = str(input('Digite o nome do aluno: '))
lista_alunos = [a1, a2, a3, a4]
escolhido = random.choice(lista_alunos)
#Retorna um elemento aleatório da sequência não vazia (alunos). Se (alunos) estiver vazio, IndexError.
print()
print('O aluno escolhido foi: {}'.format(escolhido))
