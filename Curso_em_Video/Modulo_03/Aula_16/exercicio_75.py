'''
    75 - Desenvolva um programa que leia 4 valores no teclado e seja colocado em uma tupla. No final, mostre:
        a) Quantas vezes aparece o valor 9;
        b)Em que posição foi digitado o primeiro valor 3
        C) Quais foram os números pares
'''
'''
while True:
    try:
        valores = []
        for p in range(1, 5): # o priemiro número marca o inicio do indice e o segunda e a quantidades de "voltas" que o loop deve dar
            valor = int(input(f'{p}° valor: '))
            valores.append(valor)
'''
            
valores = (int(input('Digite um valor:')), 
           int(input('Digite um valor:')),
           int(input('Digite um valor:')),
           int(input('Digite um valor:')))
print(valores)
print('------------------------------------')
print (f'1| Quantas vezes aparece o valor 9: {valores.count(9)}')
if 3 in valores:
    print (f'2| Em que posição foi digitado o primeiro valor 3: {valores.index(3)+1}')
else:
    print('2| Em que posição foi digitado o primeiro valor 3: O valor 3 não foi digitado.')
print (f'3| Quais foram os números pares:')
for n in valores:
    if n % 2 == 0:
        print(n, end=', ')
