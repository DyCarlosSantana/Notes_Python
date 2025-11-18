#Padrão ANSI - Normalização Internacional
#\033[...m
#Style - 0 = none, 1 = bold, 4 = underline, 7 = negative
#Text - 30 a 37 ----- branco, vermelho, verde, amarelo, azul, roxo, ciano, cinza.
#Background - 40 a 47

#Exemplo \033[0;33;44m
'''
print('\033[0;30;41mTeste01')
print('\033[1;35;46mTeste01')
print('\033[4;32;47mTeste01')
print('\033[0;33;44mTeste01')
'''

nome = str(input('Nome:'))
print('Olá,{}{}{}'.format('\033[0;34m', nome, '\033[m'))

#Tecnica
cores = {'limpa':'\033[m',
         'amarelo':'\033[33m',
         'Azul': '\033[34m',
         'verde': '\033[32m',
         'vermelho': '\033[31m'}
nome = str(input('Nome:'))
print('Olá,{}{}{}'.format(cores['vermelho'], nome, cores['limpa']))