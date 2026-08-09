#Faça um programa que leia a idade de um jovem e informe, de acordo com sua idade: Se ele ainda vai se alistar ao serviço militar; Se é a hora de se alistar, ou se ja passou do tempo do alistameto.
#Seu programa tambem deverá mostrar o tempo que falta ou que passou do prazo.
from datetime import date
ano_atual = date.today().year
ano_nascimento = int(input('Ano de nascimento: '))
idade = ano_atual - ano_nascimento
alistamento = 18

if idade == alistamento:
    print('Você ja completou {} ano(s).'.format(idade))
    print('Esta na hora de realizar seu alistamento militar')
elif idade < alistamento:
    verificacao = alistamento - idade
    print('Você ainda irá realizar seu alistamento militar')
    print('Ainda falta {} ano(s).'.format(verificacao))
    print('Seu alistamento será em {}'.format(ano_atual + verificacao))
elif idade > alistamento:
    verificacao = idade - alistamento
    print('Já passou da hora de realizar seu alistamento militar')
    print('Já passou {} ano(s), do periodo de alistamento.'.format(verificacao))
    print('Seu alistamento foi em {}'.format(ano_atual - verificacao))