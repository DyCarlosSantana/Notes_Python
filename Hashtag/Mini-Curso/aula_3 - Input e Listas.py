#INPUT
faturamento = float(input('Informe o faturamento: '))

custo = float(input('Informe o custo: '))

lucro = faturamento - custo
print(lucro)
print('___'*20)
print('')
#LISTAS
lista_vendas = [100, 50, 1000, 800, 35]
print(lista_vendas) #imprime os itens da lista
print(lista_vendas[3]) #seleciona um dos elementos da lista
print(lista_vendas[-1]) #cantagem inversa --> inicia pelo ultimo item

qtd_vendas = len(lista_vendas) #verifica o 'tamanho da lista' quantos itens existem dentro dela.
print(qtd_vendas)

total_vendas = sum(lista_vendas) #função (sum = soma), soma todos os itens da lista.
print(f'valor total: R$ {total_vendas}')
#volar maximo 
print(f"valor maximo: R${max(lista_vendas)}") 
#valor minimo
print(f'valor minimmo: R${min(lista_vendas)}') 
#média
print(f'Media: R$ {total_vendas / qtd_vendas}')

##OUTROS METODOS PARA LISTA
#encontrar um elemento (posição do elemento)
lista_produtos = [ 'iphoene', 'ipade', 'apple watch', 'airpods', 'macbook']
print('macbook' in lista_produtos) #verifica se o item esta na lista

posicao = lista_produtos.index('airpods') #procura o item na lista_produtos
print(posicao)
pedaco_lista = lista_produtos[posicao:] #pega apena pedaços da lista
print(pedaco_lista)

#edita um item
lista_precos = [5000, 7000, 3000, 1000, 10000]
lista_preco = lista_precos[0] * 10 / 100
print(lista_precos)

#remove um item da lista
lista_produtos.remove('macbook') #você repassa o valor do item que quer remover 'macbook'
print(lista_produtos) 
lista_produtos.pop(2) #você repassa a posição do item que quer reover [2]
#item_removido = lista_produtos.pop(1) ##armazena o item removido
print(lista_produtos)
#print(item_removido)

#Adicionando um item na lista
lista_produtos.append('macbook')
lista2_produtos = ['PC', 'air tag', 'caixa de som']
#lista_produtos.append(lista2_produtos) ##adciona uma lista em outra como um item sendo diferente do '.extend'
lista_produtos.extend(lista2_produtos)
print(lista_produtos)

#adicionando um item em uma posição especifica
lista_produtos.insert(1, 'airpod max') #insere o novo item na lista em uma posição especifica
print(lista_produtos)

#contar quantas vezes um item aparece
print(lista_produtos.count('airpods'))

#ordenar uma lista
lista_produtos.sort() #sort = ordenar --> por padrão esse metodo ordena na ordem crescente 
#no caso de str em ordem alfabetica (ASCII) tabela de programação, as letras maiusculas vem antes das minusculas
print(lista_produtos)
lista_precos.sort()
print(lista_precos)
lista_precos.sort(reverse=True) # para reverter a ordem (ordem contraria) usar o modo (reverse=True)
print(lista_precos)

#funções --> Tuplas e Dicionarios... (proxima aula) 