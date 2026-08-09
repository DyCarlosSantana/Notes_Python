#Faça um programa que calcule a soma entre todos os números impares que são multiplos de três e que se encontram no intervalo de 1 até 500.

soma = 0 #Acumulador geralmente soma valores
cont = 0 #Contador conta as repetições

for c in range(1, 501, 2): #contagem
    if c % 3 == 0:   #Se for multiplo de 3
        cont = cont + 1   #conta os numeros impares multiplos de 3. (cont += 1)
        soma = soma + c   #(soma += c)

print('A soma de todos os {} valores solicitados é: {}'.format(cont, soma)) #A soma deve ser 20667
print('Fim')