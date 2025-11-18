# Desafio 68: Jogo do Par ou Ímpar
# Objetivo:
# Criar um jogo onde o usuário escolhe par ou ímpar e joga contra o computador.
# O jogo só é interrompido quando o jogador perder.
# No final, mostrar:
# Quantas vitórias consecutivas o jogador teve.

from random import randint
cont = 0
print('====='*5)
print("VAMOS JOGAR PAR OU IMPAR")
print('====='*5)

while True:
    num = int(input('Digite um valor: '))
    escolha_jogador = ' '
    computador = randint(0, 10)
    total = num + computador
    print('====='*5)

    while escolha_jogador not in 'PI':
        escolha_jogador = str(input('Par ou Impar [P/I]:')).strip().upper()[0]

    resultado = ' '
    venceu = False
    if (total % 2 == 0 and escolha_jogador == 'P') or (total % 2 == 1 and escolha_jogador == 'I'):
        resultado = f'Deu {"PAR" if total % 2 == 0 else "IMPAR"}, você venceu!'
        venceu = True
        cont += 1
    else:
        resultado = f'Deu {"PAR" if total % 2 == 0 else "IMPAR"}, você Perdeu!'
        venceu = False

    #Apresentação do resultado  
    print('====='*5)
    print(f'Computador Jogou: {computador}')
    print(f'Você Jogou: {num}')
    print(f'Total: {total} → {resultado}')
    print('====='*5)
    if not venceu:
        print(f'\nGAME OVER! Você venceu {cont} vezes consecutivas!')
        break
    else:
        print('Continue para a próxima rodada...\n')
