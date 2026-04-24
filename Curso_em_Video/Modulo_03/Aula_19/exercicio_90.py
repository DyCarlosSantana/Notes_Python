# Este é o arquivo número 90
#O que fazer: Faça um programa que leia nome e média de um aluno, guardando também a situação (Aprovado/Reprovado) num dicionário. No final, mostre o conteúdo da estrutura no ecrã.
aluno = {}
notas = []
aluno['Nome'] = str(input('Nome do Aluno: '))
notas.append(float(input('1° Nota: ')))
notas.append(float(input('2° Nota: ')))
media = sum(notas) / 2

if media >= 7:
    status = "Aprovado"
else:
    status = "Reprovado"

aluno['Notas'] = notas
aluno['Media'] = media
aluno['Status'] = status

for c, v in aluno.items():
    print(f'{c}: {v}')

#Adicionei as caleta de duas notas, encapsuladas em uma lista (notas), e será exibida em conjunto com a média final, assim como a situação/status.