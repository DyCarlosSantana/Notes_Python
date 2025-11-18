# faturamento = float(input('Insira o valor do faturamento: '))
# custo = float(input('Insira o valor dos custos: '))
# lucro = faturamento - custo

#identação # condição/comparação 

# if lucro >= 0:
#     print(f'Lucro de R${lucro:.2f}')
# else:
#     print(f'Prejuizo de R${lucro:.2f}')
# print('Acabou!')

#EXEMPLOS
produtos = ['Iphone', 'Ipad', 'Airpod']
novo_produto = str(input('Digite  o nome do produto: ')).capitalize()

if novo_produto in produtos:
    print('Produto ja existe na lista de produtos!')
else:
    produtos.append(novo_produto) #append = acrescentar (tradução literal)
    print('Produto cadastrado com sucesso!')
print(produtos)

print('___'*20)
print(' ')
#EXEMPLOS 02
#Bonus para funcionarios
#Vendas maiores do que 15.000, então ganha 500 de bonus
#Vendas entre 5.000 e 15.000, então ganha 100 de bonus
#Vendas menores que 5.000, não ganha bonus.

vendas_funcionarios = float(input('Valor das vendas: '))
if vendas_funcionarios >= 15000:
   bonus = 500
elif vendas_funcionarios >= 5000:
    bonus = 100
else:
    bonus = 0
print(f'Bonus adicional do Funcionario: {bonus}')

print('___'*20)
print(' ')
#EXEMPLOS 02
#Bonus para funcionarios
#Vendas maiores do que 15.000, então ganha 500 de bonus
#Vendas entre 5.000 e 15.000, então ganha 100 de bonus
#Vendas menores que 5.000, não ganha bonus.
#So ganha bonus se as vendas totais da empresa forem maiores que 100.000

vendas_empresa = float(input('Vendas da Empresa: '))
meta_empresa = 100000

vendas_funcionarios = float(input('Valor das vendas: '))
if vendas_funcionarios >= 15000 and vendas_empresa >= meta_empresa: #usando o "AND"
   bonus = 500
elif vendas_funcionarios >= 5000 and vendas_empresa >= meta_empresa:
    bonus = 100
else:
    bonus = 0

print(f'Bonus adicional do Funcionario: {bonus}')