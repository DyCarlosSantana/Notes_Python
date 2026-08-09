# Este é o arquivo número 91
#O que fazer: Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios. Guarde esses resultados num dicionário em Python. No final, coloque esse dicionário em ordem, sabendo que o vencedor tirou o maior número no dado.
#Dica do Cleitin: Vais precisar de usar o itemgetter da biblioteca operator para ordenar o dicionário.
from random import randint
from time import sleep
from operator import itemgetter

jogo = {
    'Jogador_01': randint(1, 6),
    'Jogador_02': randint(1, 6),
    'Jogador_03': randint(1, 6),
    'Jogador_04': randint(1, 6)}

print('==+=='*8)
print('               RODANDO DADO               ')
for c, v in jogo.items():
    print(f'{c} tirou {v}')
    sleep(1)

ranking = []
ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True)
print('==+=='*8)
print('               RANKING               ')
for index, j in enumerate(ranking, start=1):
    print(f'{index}° Lugar: {j[0]} com {j[1]}')
    sleep(1)

'''
Organização: Usamos a função sorted combinada com o módulo operator.itemgetter. Isso permite ordenar pelos valores (índice 1) em vez das chaves
'''