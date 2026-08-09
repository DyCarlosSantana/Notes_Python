# for i in range(2): #ou deixar mais especificado (0, 5)
#     print(i)
#     print('Usando uma estrutura de repetição')

lista_precos = [1500, 1000, 800, 2000]

#_______________________________________________________________

#taxa_imposto = 0.1 #10%

# for preco in lista_precos:
#     imposto = preco * taxa_imposto
#     print(f'Preço do Produto {preco}, Imposto de {imposto}')

#_______________________________________________________________

#Exemplos
#Para produtos de ATÈ 1000, pagam 10% de imposto
#Para produtos acima de 1000, pagam 15% de imposto
for preco in lista_precos:
    if preco <= 1000:
        taxa_imposto = 0.1 #10%
    elif preco > 1000:
        taxa_imposto = 0.15 
    imposto = preco * taxa_imposto
    print(f'Valor do produto: {preco}, Imposto: {imposto}')
print('_____'*10)
#_______________________________________________________________

#Exemplos 02
#Mesma regra de imposto
#Somar todos o valor de todos os impostos

total_imposto = 0
for preco in lista_precos:
    if preco <= 1000:
        taxa_imposto = 0.1
    elif preco > 1000:
        taxa_imposto = 0.15
    imposto = preco * taxa_imposto
    total_imposto += imposto  #O mesmo que (total_imposto = total_imposto + imposto)
    print(f'Valor do produto: {preco}, Imposto: {imposto}')
    print(f'Total de Imposto: {total_imposto}')
print('_____'*10)
#_______________________________________________________________

#Exemplos 03 - Estrutura de Repetição + dicionarios
vendas_23 = {'jan': 15000, 'fev': 10000, 'mar': 5000}
vendas_24 = {'jan': 16000, 'fev': 11000, 'mar': 5100}

#Calculo percentual de crescimento
#16000 / 15000 - 1 -> quanto % eu cresci de um ano para o outro
for mes in vendas_24: #Por padrão a variavel do for (mes) vai receber sempre a chave do dicionario e não o valor
    valor_23 = vendas_23[mes]
    valor_24 = vendas_24[mes]
    crescimento = valor_24 / valor_23 - 1
    print(f'No mes de {mes}, o crescimento foi de {crescimento:.1%}')
