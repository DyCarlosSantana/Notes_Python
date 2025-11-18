#Crie um programa que leia duas notas de aluno e calcule sua média, mostrando uma mensagem no final, de acordo com a média atingida.
#Média abaixo de 5.0 - Reprovado
#Média entre 5.0 e 6.9 - Recuperação
#Média 7.0 ou superior - Aprovado

n1 = float(input('Insira sua primeira nota: '))
n2 = float(input('Insira sua segunda nota: '))
media = (n1 + n2) / 2
if media < 5:
    print('Média do Aluno: {:.1f}'.format(media))
    print('REPROVADO')
elif 7 > media >= 5:
    print('Média do Aluno: {:.1f}'.format(media))
    print('RECUPERAÇÂO')
elif media >= 7:
    print('Média do Aluno: {:.1f}'.format(media))
    print('APROVADO')
else:
    print('Tente novamente')