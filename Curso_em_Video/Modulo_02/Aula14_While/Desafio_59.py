#Crie um programa que leia dois valores e mostre um  menu ma tela:
# [1]somar
# [2]multiplicar
# [3]maior
# [4]novos numeros
# [5]sair do programa
#Seu programa deverá realizar a operação solicitada em cada caso.

while True:
    valor1 = int(input('Digite o 1° valor: '))
    valor2 = int(input('Digite o 2° valor: '))

    while True:
        print('''
        OPÇÕES DISPONIVEIS:
        [1]somar
        [2]multiplicar
        [3]maior
        [4]novos numeros
        [5]sair do programa''')
        opcao = input('\nEscolha uma opção: ').strip()
        #  Verifica se o valor de 'opcao' não está na lista de opções válidas. 
        if opcao not in ['1', '2', '3', '4', '5']: 
            print('Opção invalida!')
            continue  # Ignora o código abaixo e volta para o início do loop  

        opcao = int(opcao)
        if opcao == 1:
            resultado = valor1 + valor2
            print(f'{valor1} + {valor2} = {resultado}')
        elif opcao == 2:
            resultado = valor1 * valor2
            print(f'{valor1} x {valor2} = {resultado}')
        elif opcao == 3:
            resultado = valor1 if valor1 > valor2 else valor2
            print(f'O maior valor é: {resultado}')
        elif opcao == 4:
            print('Escolha novos valores...')
            break  # Sai do loop do menu e volta para pedir novos números    
        elif opcao == 5:
            print('Encerrando programa...')
            exit()  # Fecha o programa, dever ser usado quando não há mais nada a ser executado e o programa deve terminar.
        input('\nPressione Enter para continuar...')
print('Fim.')

# ANOTAÇÕES
# Comparação Rápida:

## continue vs break:
#### continue: "Pula esta rodada, vou para a próxima".
#### break: "Chega, saio deste loop agora!".

## exit() vs break:
#### exit(): Mata o programa.
#### break: Sai apenas de um loop.
     
    