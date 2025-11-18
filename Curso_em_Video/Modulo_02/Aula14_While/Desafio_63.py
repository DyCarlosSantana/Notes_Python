#Escreva um programa que leia um numero n inteiro qualquer que mostre na tela os n primeiros termos de uma sequencia de Fibonacci.
cont = 0
soma = 0
print('-'*30)
print('Sequencia de Fibinacci')
print('-'*30)
num = int(input('Digite um número: '))
t1 = 0
t2 = 1
print(f'{t1} -> {t2}', end='')
cont = 3
while cont <= num:
    t3 = t1 + t2
    print(f' -> {t3}', end='')
    t1 = t2
    t2 = t3
    cont += 1
print(' FIM')