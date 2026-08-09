import random
import time
n = random.randint(0, 5)
print('-=-'*20)
print('vou pensar em um número entre 0 e 5. Tente adivinhar...')
print('-=-'*20)
jogador = int(input('Faça seu chute: '))
print('PROCESSANDO...')
time.sleep(1)
if jogador == n:
    print('Pensei no número {}'.format(n))
    print('Vocé acertou!')
else:
    print('Pensei no número {}'.format(n))
    print('Você Errou!')
