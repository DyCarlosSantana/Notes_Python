# Este é o arquivo número 93
#O que fazer: Crie um programa que gira o aproveitamento de um jogador de futebol. O programa vai ler o nome do jogador e quantas partidas ele jogou. Depois vai ler a quantidade de gols feitos em cada partida. Tudo isso será guardado num dicionário, incluindo o total de gols feitos durante o campeonato.

dados = {}
gols = []

dados['Nome'] = str(input('Nome do Jogador: '))
dados['Partidas'] = int(input('Partidas Jogadas: '))

for i in range(1, dados['Partidas']+1):
    gols.append(int(input(f'Gols feitos na {i}° Partida: ')))

dados['Gols por partida'] = gols
total = sum(gols)
dados["Total de Gols"] = total

print('')
print('==+=='*8)
for c, v in dados.items():
    print(f'{c}: {v}')