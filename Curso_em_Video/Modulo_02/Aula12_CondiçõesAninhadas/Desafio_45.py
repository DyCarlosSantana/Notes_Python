#Crie um programa que faça o computador jogar Jokenpô com você.
import random
import time
print('{:=^15}'.format('VAMOS JOGAR'))
print('{:_^15}'.format('JOKENPÔ'))
opcoes = ['PEDRA', 'PAPEL', 'TESOURA']
computador = random.randint(0, 2)

print('''Suas opções:
[0] PEDRA
[1] PAPEL
[2] TESOURA''')
jogador = int(input('Qual vai ser a sua jogada? '))
print('JO')
time.sleep(0.5)
print('KEN')
time.sleep(0.5)
print('PÔ')

print('_'*15)
print('O computador jogou: {}'.format(opcoes[computador]))
print('Você jogou: {}'.format(opcoes[jogador]))
print('-'*15)
if computador == 0: #Computador jogou Pedra
    if jogador == 0:
        print('Empate!')
    elif jogador == 2:
        print('Computador Vencel!')
    elif jogador == 1:
        print('Você Vencel!')
elif computador == 1: #Computador Jogou Papel
    if jogador == 1:
        print('Empate!')
    elif jogador == 0:
        print('Computador Vencel!')
    elif jogador == 2:
        print('Você Vencel!')
elif computador == 2:  #Computador jogou Tesoura
    if jogador == 2:
        print('Empate!')
    elif jogador == 1:
        print('Computador Vencel!')
    elif jogador == 0:
        print('Você Vencel!')
else:
    print('Opção invalida, Tente novamente')