#Faça um programa que mostre na tela uma contagem regressiva para o estoura de fogos de artificio, indo de 10 a 0, com uma pausa de 1s entre eles.

import time

for c in range(11,0, -1): #inverção de posição
    print(c)
    time.sleep(1)
print('Fogos e tal')