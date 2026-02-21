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
            print('Valor adicionado!')
        else:
            print('Valor duplicado! Não foi adicionado')

        sn = input('Deseja continuar [S/N]-> ')
        if sn in 'Nn':
            break
        elif sn in 'Ss':
            continue

    except:
        print('Tente novamente!', end=' ')

valores.sort()
print(f'Os números digitados foram: {valores}')

    
    
