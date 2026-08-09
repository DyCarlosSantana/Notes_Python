'''
    76 - Crie programa que tenha uma tupla unica com nomes de produtos e seus respectivos preçõs na sequencia. No final, mostre uma listagem de preços organizados em forma tabular.
'''
listagem = ('Caderno', 28.50, 
            'Estojo', 15.00, 
            'Lápis', 1.25, 
            'Caneta', 2.50, 
            'Marcador de texto', 5.00, 
            'Mochila', 110.00, 
            'Lápis de Cor', 8.00, 
            'Cola', 5.50, 
            'Borracha', 1, 
            'Apontador', 1)

print('-'*40)
print(f'{"LISTAGEM DE PREÇOS":^40}')
print('-'*40)
for position in range(0, len(listagem)):
    if position % 2 == 0:
        print(f'{listagem[position]:.<30}', end='')
    else:
        print(f'R${listagem[position]:>7.2f}')
print('-'*40)