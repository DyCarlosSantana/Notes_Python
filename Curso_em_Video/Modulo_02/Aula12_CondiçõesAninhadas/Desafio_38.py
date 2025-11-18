#Escreva um programa que leia dois numeros inteiros e compareos, mostrando na tela uma mensagem:
#O primeiro valor é maior ou o segundo valor é maior ou Não existe valor maior, os dois são iguais.

n1 = int(input('Digite o primeiro valor: '))
n2 = int(input('Digite o segundo valor: '))

if n1 > n2:
    print('O primeiro valor é o maior'.format(n1))
elif n2 > n1:
    print('O segundo valor é maior'. format(n2))
else:
    print('Não existe valor maior, os dois valores informados são iguais ({})'.format(n1, n2))