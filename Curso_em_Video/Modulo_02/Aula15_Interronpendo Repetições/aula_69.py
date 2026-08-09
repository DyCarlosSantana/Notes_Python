# Desafio 69: Análise de Dados
# Objetivo:
# Ler a idade e o sexo de várias pessoas.
# O programa pergunta se o usuário quer continuar após cada cadastro.
# No final, mostrar:
# Quantas pessoas têm mais de 18 anos.
# Quantos homens foram cadastrados.
# Quantas mulheres têm menos de 20 anos.

cont_idade = 0
cont_homens = 0
cont_mulheres = 0
print('-'*25)
print('CADASTRO DE PESSOAS')
print('-'*25)
while True:
    idade = int(input('Idade: '))
    while sexo not in "MF":
        sexo = str(input('Sexo [M/F]: ')).upper().strip()[0]
        print(' ')

    #Anlise dos dados coletados 
    if idade >= 18:
        cont_idade +=1
    if sexo == 'M':
        cont_homens += 1
    if idade < 20 and sexo == 'F':
        cont_mulheres += 1

    #Condição de parada
    prox = str(input('Para prosseguir precione [ENTER]...\nPara encerrar digite [0]\n'))
    print('-'*25)
    if prox == '0':
        break
#Apresentação dos dados coletados:
print(f'Total de pessoas com mais de 18 anos: {cont_idade}')
print(f'Total de homens cadastrados: {cont_homens}')
print(f'Total de mulheres com menos de 20 anos: {cont_mulheres}')
print('-'*25)
print('Programa Encerrado!')