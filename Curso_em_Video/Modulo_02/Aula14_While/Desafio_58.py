#Melhore o jogo do desafio 29 onde o computador vai "Pensar" em um núemro de 0 a 10. Só que agora o jogador vai tentra adivinhar até acertar, mostrando no final quantos palpites foram necessarios para vencer.
import random
print('---'*20)
print('Vou pensar em um número entre 0 e 10. Tente adivinhar...')
computador = random.randint(0, 11)
palpites = 0
acertou = False
while not acertou: #Enquanto não for verdadeiro...
    jogador = int(input('Faça seu chute: '))
    palpites += 1
    if jogador == computador:
        acertou = True 
    else:
        if jogador < computador:
            print(f'Mais... Tente novamente')
        elif jogador > computador:
            print(f'Menos... Tente novamente')
print(f'Você acertou com {palpites} tentativa(s)')
print('---'*20)