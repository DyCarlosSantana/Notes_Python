"""
Exercício 88: Palpites para a Mega Sena
O que fazer: Faça um programa que ajude um jogador da Mega Sena a criar palpites. O programa vai perguntar quantos jogos serão gerados e vai sortear 6 números entre 1 e 60 para cada jogo, registando tudo numa lista composta.
"""

from random import randint
from time import sleep

jogos = []
palpite = []

qtd_jogos = int(input("Quantos jogos devem ser gerados: "))

cont = 1
while cont <= qtd_jogos:
    for n in range(0, 6):
        palpite.append(randint(1, 60))
    jogos.append(palpite[:])
    palpite.clear()
    cont += 1
        
for index, palpite in enumerate(jogos):
    print(f"Jogo {index+1}: {palpite}")
    sleep(1)