'''
Exercício 82: Dividindo Valores em Várias Listas
O que fazer: Crie um programa que vai ler vários números e colocar numa lista. Depois disso, crie duas listas extras que vão conter apenas os valores pares e os valores ímpares digitados, respetivamente. Ao final, mostre o conteúdo das três listas geradas.
'''
lista = []
par = []
impar = []
while True:
    try:
        num = int(input('Digite um número: '))
        lista.append(num)
        if num % 2 == 0:
            par.append(num)
        else:
            impar.append(num)

        sn = input('Deseja continuar: [S/N]-> ').upper()
        if sn == 'N': 
            break
        elif sn == 'S':
            continue
    except:
        print(f'Tente Novamente!', end=' ')

print(f'Lista Completa: {lista}')
print(f'Números Pares: {par}')
print(f'Números Impares: {impar}')
