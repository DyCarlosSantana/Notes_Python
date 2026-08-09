# Desafio 70: Estatísticas em Produtos
# Objetivo:
# Ler o nome e preço de vários produtos.
# O programa pergunta se o usuário quer continuar após cada cadastro.
# No final, mostrar:
# Total gasto na compra.
# Quantos produtos custam mais de R$ 1000.
# Nome do produto mais barato.
lista_produtos = []
total_gasto = 0
acima_1000 = 0
menor_preco = float('inf') #Inicializa a variavel com um valor infinito
nome_menor_preco = ' '
preco_total = 0

print('-'*25)
print('CAIXA - SUPER MERCADO')
print('-'*25)
while True:
    produto = str(input('Produto: ')).capitalize().strip()
    preco = float(input('preco: R$ '))

    lista_produtos.append({'nome': produto, 'preco': preco}) #dicionario

    total_gasto += preco

    #menor preço e precço acima de 1000
    if preco > 1000:
        acima_1000 += 1
    if preco < menor_preco:
        menor_preco = preco
        nome_menor_preco = produto

    print('_'*25)
    while True:
        prox = str(input('Gostaria de continuar? [S/N]\n')).upper().strip()[0]
        if prox in ('S', 'N'):
            break

    if prox == "N":
        break
    print('_'*25)

#Apresentação do resultado
print(' ')
# Dentro da seção de resultados, adicione:
print('\n' + '-' * 15, 'PRODUTOS', '-' * 15)
if len(lista_produtos) == 0: #analisa a lista de produtos com o (len)
    print("Nenhum produto cadastrado.")
else:
    #Para cada indice e produto enumerado na lista começando pelo 1°:
    for indice, produto in enumerate(lista_produtos, start=1): #Enumerate gera um índice automático para cada produto, usar o "start=1"
        print(f"{indice}. {produto['nome']} → R$ {produto['preco']:.2f}")
print('-' * 50)

print(f'preco total: {total_gasto:.2f}')
print(f'Qtd produtos acima de R$1.000: {acima_1000}')
print(f'Produto mais barato: {nome_menor_preco} → R$ {menor_preco}')