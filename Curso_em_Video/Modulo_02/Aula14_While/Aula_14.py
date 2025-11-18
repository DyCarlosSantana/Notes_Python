#Estrutura de repetição com teste lógico

# for c in range(1, 11): #Estrutura de repetição com variaveis de controle
#     print(c)
# print('Fim')

c = 1
while c < 11:
    print(c)
    c = c + 1
print('Fim')

lista_valores =[]
r = 'S'
while r == 'S':
    n = int(input('Digite um número: '))
    lista_valores.append(n)
    r = str(input('Quer continuar? [S/N]:')).upper().strip()
print(lista_valores)
print('Fim')

par = 0
impar = 0
n = 1
while n != 0:
    num = int(input('Digite um núemro: '))
    if n != 0:
        if n % 2 == 0:
            par += 1
        else:
            impar += 1
print(f'Você digitou {par} números pares, e {impar} números impares')
print('Acabou')