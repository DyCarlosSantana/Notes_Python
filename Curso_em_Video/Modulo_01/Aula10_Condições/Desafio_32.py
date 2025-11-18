# Desafio 32: Faça um programa que leia um ano qualquer e mostre se ele é bissexto.
# Para saber se um ano é bissexto, é necessário que ele seja divisível por 4, mas não por 100, exceto se ele for divisível por 400.

from datetime import date
ano = int(input('Qual ano você quer analisar? Coloque 0 para analisar o ano atual:'))
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0: # != sinal de diferente em python.
    print('O ano {} é BISSEXTO'.format(ano))
else:
    print('O ano {} NÃO é BISSEXTO'.format(ano))
print('Fim do programa')
print('-=-' * 15)