# Desafio 67: Tabuada v3.0
# Objetivo:
# Criar um programa que mostre a tabuada de vários números.
# O programa deve:
# Parar quando o número digitado for negativo.
# Mostrar a tabuada do número digitado.

print('================= TABUADA DIGITAL =================')
print('[Para encerra o programa digite um número negativo]')
while True:
    print('_____'*10)
    num = int(input('DIGITE UM NÚMERO: '))
    print('_____'*10)
    if num <0:
        print('Programa Encerrado.')
        break
    print('''OPÇÕES:
Soma [1]
Subtração [2]
Multiplicação [3]
Divisão [4]
''')
    opicao = int(input('DIGITE SUA ESCOLHA: '))
    if opicao == 1:
        print('_____'*10)
        print('[SOMA]')
        for c in range(1, 11):
            resultado = num + c
            print(f'{num} + {c} = {resultado}')
    elif opicao == 2:
        print('_____'*10)
        print('[SUBTRAÇÃO]')
        for c in range(1, 11):
            resultado = num - c
            print(f'{num} - {c} = {resultado}')
    elif opicao == 3:
        print('_____'*10)
        print('[MULTIPLICAÇÃO]')
        for c in range(1, 11):
            resultado = num * c
            print(f'{num} x {c} = {resultado}')
    elif opicao == 4:
        print('_____'*10)
        print('[DIVISÃO]')
        for c in range(1, 11):
            resultado = num / c
            print(f'{num} / {c} = {resultado}')
    else:
        print('Opção Invalida! Tente novamente...')
    print('_____'*10)
    input('Precione ENTER para continua...')
