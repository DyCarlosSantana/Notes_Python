#Crie um programa que leia o ano de nascimento de 7 pessoas. No final mostre quantas pessoas ainda não atingiram a maioridade e quantas já sõa maiores.
import datetime

cont = 0 #contador
menor_idade = 0 #Acumulador (menores de idade)
maior_idade = 0 #Acumulador (maiores de idade)

for c in range(1, 5): #Laço (for) para coletar os anos e verificar as idades
    ano = int(input('Ano de Nascimento da {}° pessoa: '.format(c)))
    idade = datetime.date.today().year - ano #Ano tual - o ano de nascimento.
    if idade < 18:
        menor_idade += 1
    else:
        maior_idade += 1
    cont += 1
print('='*30)
print('''Das {} pessoas, temos {} pessoa(s) maior de idade, e {} pessoa(s) menor de idade.'''.format(cont, maior_idade, menor_idade))