'''
    75 - Desenvolva um programa que leia 4 valores no teclado e seja colocado em uma tupla. No final, mostre:
        a) Quantas vezes aparece o valor 9;
        b)Em que posição foi digitado o primeiro valor 3
        C) Quais foram os números pares
'''
while True:
    try:
        valores = []
        for p in range(1, 5): # o priemiro número marca o inicio do indice e o segunda e a quantidades de "voltas" que o loop deve dar
            valor = int(input(f'{p}° valor: '))
            valores.append(valor)

        print(valores)
        print('------------------------------------')
        print (f'1|Quantas vezes aparece o valor 9: {valores.count(9)}')
        print (f'2|Em que posição foi digitado o primeiro valor 3: {valores.index(3)}')
        par = []
        for n in valores:
            if n % 2 == 0:
                par.append(n)
        print (f'3|Quais foram os números pares: {par}')
        break
    except:
        print('Tente novamente!')
