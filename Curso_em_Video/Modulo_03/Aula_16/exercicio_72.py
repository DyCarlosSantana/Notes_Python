'''
    72 - Crie um programa que tenha uma tupla totalmente preenchida com uma contagem por extenso, e zero até vinte. Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostra-lo por entenso;
'''
numeros_extenso = ('zero', 'um', 'dois', 'três', 'quadro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'catorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')
while True:
    while True:
        num_usuario = int(input('Digite um número entre 0 e 20: '))
        if 0 <= num_usuario <= 20:
            break
        print('Tente novamente! ', end='')
            
    print(f'Você digitou o número {numeros_extenso[num_usuario]}')
    prosseguir = input('Encerrar [q], Continuar [Enter] -> ')
    if prosseguir == 'q' or 'Q':
        break