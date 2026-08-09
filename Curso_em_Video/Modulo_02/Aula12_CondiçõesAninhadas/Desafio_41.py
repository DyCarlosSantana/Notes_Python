#A confraternização nacional de natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria de acordo com sua idade:
# Até 9 anos - mirim
# Até 14 anos - infantil
# Até 19 anos - junior
# Até 20 anos - senior
# Acima - master
import datetime #biblioteca para verificação do ano atual
nome = str(input('Insira seu nome: ')).upper()
ano_nascimento = int(input('Insira o ano de nascimento: ')) 
ano_atual = datetime.date.today().year
idade = ano_atual - ano_nascimento
#Verificação de categoria
if idade <= 9:
    categoria = ('MIRIN')
elif idade <= 14:
    categoria = ('INFANTIL')
elif idade <= 19:
    categoria = ('JUNIOR')
elif idade <= 20:
    categoria = ('SENIOR')
elif idade > 20:
    categoria = ('MASTER')
#Impressão dos dados
print('-=-'*15)
print('NOME: {}'.format(nome))
print('CATEGORIA: {}'.format(categoria))
print('-=-'*15)