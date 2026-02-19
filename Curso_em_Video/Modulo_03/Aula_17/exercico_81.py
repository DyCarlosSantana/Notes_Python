'''
Exercício 81: Extraindo Dados de uma Lista
O que fazer: Crie um programa que vai ler vários números e colocar numa lista. Depois disso, mostre:
    1. Quantos números foram digitados.
    2. A lista de valores, ordenada de forma decrescente.
    3. Se o valor 5 foi digitado e está ou não na lista.
'''
lista = []
while True:
    try:
        lista.append(int(input('Digite um número: ')))
        sn = input('Deseja continuar: [S/N]-> ').upper()
        if sn == 'N': 
            break
        elif sn == 'S':
            continue
    except:
        print(f'Tente Novamente!', end=' ')

print(f'Foram digitados {len(lista)} números;')

lista.sort(reverse=True)
print(f'Os números digitados forma: {lista}')

if 5 in lista:
    print('O número 5 faz parte da lista')
else:
    print('O número  não foi digitado')