'''
    75 - Desenvolva um programa que leia 4 valores no teclado e seja colocado em uma tupla. No final, mostre:
        a) Quantas vezes aparece o valor 9;
        b)Em que posição foi digitado o primeiro valor 3
        C) Quais foram os números pares
'''
while True:
    try:
        n1 = int(input('Digite o primeiro valor: '))
        n2 = int(input('Digite o segundo valor: '))
        n3 = int(input('Digite o terceiro valor: '))
        n4 = int(input('Digite o quarto valor: '))
        valores_recolhidos = n1, n2, n3, n4
        print(valores_recolhidos)
        print('------------------------------------')
        print (f'1|Quantas vezes aparece o valor 9: {valores_recolhidos.count(9)}')
        print (f'2|Em que posição foi digitado o primeiro valor 3: {valores_recolhidos.index(3)}')
        par = []
        for n in valores_recolhidos:
            if n % 2 == 0:
                par.append(n)
        print (f'3|Quais foram os números pares: {par}')
        break
    except:
        print('Tente novamente!')
