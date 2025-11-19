lista_produtos = ['Ipad', 'Iphone', 'Macbook']
lista_precos = [7000, 5000, 20000]

dic_produtos = {'Ipad': 7000, 'Iphone': 5000, 'Macbook': 20000}

#Pegar um Item
# produto = 'Iphone'
# posicao = lista_produtos.index(produto)
# preco = lista_precos[posicao]
# print(produto, preco)

print(dic_produtos['Iphone'])

dic_vendas = {'Lira': [500, 1000, 1500], 'João': [500, 400, 500]}
print(dic_vendas['Lira'])

#Adicionar e Editar Itens:
dic_produtos['Iphone'] = 5500
print(dic_produtos)

dic_produtos['Ipad mini'] = 6000
print(dic_produtos)

#Remover/Excluir:
item_removido = dic_produtos.pop('Macbook')
print(dic_produtos)
print(item_removido)

#Verificar se existe um item no dicionario
print('Iphone' in dic_produtos) #procura por chaves / equvalente a ".keys.()"
print(20000 in dic_produtos.values()) #procura por valores

#criando listas a partir de dicionarios
produtos = list(dic_produtos.keys())
print(produtos)
precos = list(dic_produtos.values())
print(precos)

#conatagem de itens no dicionario
qtde = len(dic_produtos)
print(qtde)

#Exercicio:
#busca de produto
dic_produtos = {'Ipad': 7000, 'Iphone': 5000, 'Macbook': 20000, 'Xiaome Note 12': 2000, 'Xiaome Pad 6': 5000, 'Acer Nitro V15': 5000}
busca_produto = input('Nome do roduto: ').title().strip()
if busca_produto in dic_produtos:
    print('Produto encontrado...')
    print(f'Produto: {busca_produto}')
    print(f'Valor: {dic_produtos[busca_produto]}')
else:
    print('Produto não encontardo')
