#Faça um programa que leia o peso de 5 (troquei para 4 pessoas) pessoas e mostre qual  foi o maior.
maior = 0
menor = 0
pesos = [] #Lista fazia para armazenar os pesos adicionados
qtd = int(input('O peso de quantas pessoas serão cadastradas? '))
for p in range(1, qtd + 1):
    peso = float(input('{}° pessoa, Peso(Kg): '.format(p)))
    pesos.append(peso) #funcão "append = acrescentar" para acrescentar os pesos inseridos na lista.
    if p == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print('')
print('Pesos inseridos : {}'.format(pesos))
print('O maior peso: {}Kg'.format(maior))
print('O menor peso: {}Kg'.format(menor))