# Este é o arquivo número 103
"""
Exercício 103: Ficha do Jogador

O que fazer: Faça um programa que tenha uma função chamada ficha(), que receba dois parâmetros opcionais: o nome de um jogador e quantos golos ele marcou. O programa deverá ser capaz de mostrar a ficha do jogador, mesmo que algum dado não tenha sido informado corretamente (se o nome estiver vazio, assuma <desconhecido>, se os golos estiverem vazios, assuma 0).
"""

def ficha(nome_jogador="<desconhecido>", qtd_gols=0):
    print(f'O jogador {nome_jogador} fez {qtd_gols} gol(s) no campeonato.')

print("---"*10)
nome = str(input('Nome do jogador: '))
gols = str(input('Quantidade de gols: '))
if gols.isnumeric(): # Identifica se é um número
    gols = int(gols)
else:
    qtd_gols = 0
if nome.strip() == '': # strip é usado para tirar espaçamentos no inicio e fim da string
    ficha(qtd_gols=gols)
else:
    ficha(nome,gols)
