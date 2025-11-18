#Crie um programa que leia varios numeros inteiros pelo teclado, O programa so irá encerrar quando o valor digitado for '999', que é a condição de parada. No final mostre quantos números foram digitados e qual a soma entre eles sem contar o (flag)->condiçao de parada.
cont = 0
soma = 0
print('A Condição de Parada é [999]')
while True:
    num = int(input('Digite um número: '))
    if num == 999:
        break
    cont += 1
    soma += num
print(f'A quantidade de números digitados foi: {cont}')
print(f'A soma de todos os números resulta em: {soma}')
