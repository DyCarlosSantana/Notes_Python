#Desenvolva um programa que leia seis números inteiros e mostre apenas a soma daqueles que forem pares. se o valor for impar, desconsidere-o.
soma = 0
cont = 0
for c in range(1,7):
    n = int(input('Digite o {}° valor: '.format(c)))
    if n % 2 == 0:
        soma = soma + n
        cont = cont + 1 
print('Você informou {} números PARES, a soma deles é: {}'.format(cont, soma))
print('Fim')