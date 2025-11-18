#Elabore um programa que calcule o valor a ser pago por um produto considerando o seu preco normal e condições de pagamento:
# À vista dinheiro/cheque - 10% de desconto;
# À vista no cartão - 5% de desconto;
# Em até 2x no cartão - preço normal;
# 3x no cartão - 20% de juros.
valor = float(input('Insira o valor do produto: R$'))
#Formas de pagamento
print('''Formas de pagamento:
[1] À vista (dinheiro/cheque) - 10% de desconto
[2] À vista no cartão - 5% de desconto
[3] Cartão em até 2 vezes - Preço normal
[4] Cartão em 3 vezes ou mais - 20% de juros''')

#Escolha da forma de pagamento
forma_pagamento = int(input('Forma de pagamento:'))
a_vista = [1]
cartao_vista = [2]
cartao_2x = [3]
cartao_3x = [4]

#verificação
if forma_pagamento == 1:
    valor_final = valor - (valor * 10 /100)
elif forma_pagamento == 2:
    valor_final = valor - (valor * 5 /100)
elif forma_pagamento == 3: 
    valor_final = valor
elif forma_pagamento == 4: 
    valor_final = valor + (valor * 20 /100)
else:
    print('Opção Invalida, escolha um némero entre 1 e 4')

#valor final
print('-=-'*15)
print('Forma de Pagamento: [{}]'.format(forma_pagamento))
print('Valor Total: R${:.2f}'.format(valor_final))
print('-=-'*15)
