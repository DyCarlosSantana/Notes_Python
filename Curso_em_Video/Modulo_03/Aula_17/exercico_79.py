'''
Exercício 79: Valores Únicos numa Lista
O que fazer: Crie um programa onde o utilizador possa digitar vários valores numéricos e registe-os numa lista. Caso o número já exista lá dentro, ele não deve ser adicionado. No final, serão exibidos todos os valores únicos digitados, em ordem crescente.
'''

valores = []

while True:

    try:
        novo_valor = (int(input('Digite um número: ')))

        if novo_valor not in valores:
            valores.append(novo_valor)

        sn = input('Deseja continuar [S/N]-> ').upper()
        if sn == 'N':
            break
        elif sn == 'S':
            continue

    except:
        print('Tente novamente!', end=' ')

valores.sort()
print(f'Os números digitados foram: {valores}')

    
    
