#crie um programa que leia varios numeros inteiros pelo teclado, no final da execução mostre a média entre todos os valores e quais foram o maior e menor valores lidos. O programa deve perguntar aos usuario de quer ou não continuar a digitra valores.
cont = 0
total = 0
maior = 0
menor = 0
while True:
    num = int(input('Digite um número: '))
    resp = str(input('Gostaria de continuar?: [S/N] ')).upper().strip()
    total += num
    cont += 1
    if cont == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        elif num < menor:
            menor = num
    if resp == 'N':
        break
    print('-----'*5)
    
media = total / cont
print(f'A média de todos os valores inseridos é de: {media}')
print('O maior valor foi {maior}, e o menor valor foi {menor}') 
print('Programa encerrado!')
