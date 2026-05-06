# Este é o arquivo número 95
#O que fazer: Aprimore o desafio 93 para que ele funcione com vários jogadores, incluindo um sistema de visualização de detalhes do aproveitamento de cada jogador.

cadastros = []
dados = {}
gols = []

while True:
    # Coleta de dados Nome e qtd de partidas
    dados['Nome'] = str(input('Nome do Jogador: '))
    dados['Partidas'] = int(input('Partidas Jogadas: '))
    # Coleta de gols por partida
    for i in range(1, dados['Partidas']+1):
        gols.append(int(input(f'Gols feitos na {i}° Partida: ')))
    # Copia da lista com gols, somatoria
    dados['Gols'] = gols[:]
    total = sum(gols) #somatoria dos gols
    dados["Total"] = total
    # Copia dos dados e limpeza de listas
    gols.clear()
    cadastros.append(dados.copy())

    resp = str(input('Deseja continuar? [S/N]: ')).upper()
    if resp == 'N':
        break

print('')
print('==+=='*8)
print('|N° | Jogador -> Gols > Total |')
print('_____'*8)
for index, i in enumerate(cadastros):
    print(f'|{index}  |{i['Nome']} | {i['Gols']} | {i['Total']}')
print('_____'*8)

while True:
    try:
        resp = int(input('Mostrar dados de qual jogador? (999 para sair): '))
        print(resp)

        if resp == 999:
            print('Encerrando programa!')
            break
        
        if cadastros[resp] in cadastros: # Se o indice (resp) exixstir dentro da lista (cadastros) ele prossegue...
            dados_jogador = cadastros[resp].copy() # cria uma copia do dicionario com os dados do jogador selecionado
            print('==+=='*8)
            print('-- LEVANTAMENTO DO JOGADOR --')
            print(f'-- Nome do Jogador: {dados_jogador['Nome']}')
            for index, g in enumerate(dados_jogador['Gols'], start=1): # Parametro start muda o indice incial
                print(f' - Na {index}° partida fez {g}')
            print(f'-- Resultado final: {dados_jogador['Total']} gols')
        else:
            print('Jogador não encontrado. Tente novamente!')
    except:
        print('Dado Invalido. Tente Novamente!')

        