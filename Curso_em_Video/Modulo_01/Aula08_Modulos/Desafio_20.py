import random

a1 = str(input('Primeiro aluno: '))
a2 = str(input('Segundo aluno: '))
a3 = str(input('Terceiro aluno: '))
a4 = str(input('Quarto aluno: '))
lista_alunos = [a1, a2, a3, a4]
escolhido = random.shuffle(lista_alunos)
#Retorna um elemento aleatório da sequência não vazia (alunos). Se (alunos) estiver vazio, IndexError.
print()
print('A ordem de apresentação será a seguinte: ')
print ('{}'.format(lista_alunos))