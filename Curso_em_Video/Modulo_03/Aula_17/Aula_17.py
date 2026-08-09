num = [2, 5, 9, 1]

print(f'Lista Inicial:')
for i, n in enumerate(num):
    print(f'Na posição {i}, encontrei o valor: {num}')

print('\nAdicionando número 8 a lista através do método append(8)')
num.append(8) # Método usado para adiciona um novo valor a lista, sempre na ultima posição.

print('\nAdicionando o número 10 a lista através do método insert(2, 10)')
num.insert(2, 10) # Na posição 2 adicione o valor 10 - os valores são realocados para inserir o nova valor desejado na posição especifica.

print('\nOrdenando a lista com método sort()')
num.sort() # O metodo sort() organiza a lista em ordem ascendente, ordenando os elementos da lista diretamente no local (in-place), modificando a lista original diferete do metodo sorted() usando na Aula_16.
print(num)

print('\nInvertendo a lista com o parametro "reverse=True" do método sort()')
num.sort(reverse = True) # O método sort() aceita dois parametros opcionais, sendo o (reverse=True)-> Para ordenar em ordem descendente, e (Key=)-> Permite especificar um criterio de ordenação personalizado.
print(num)

print(f'\nAgora a lista tem {len(num)} elementos')

print('\nRemovendo um elemento com o Comando "del"')
del num[0] # Comando usado para apagar um valor pelo indice/posição

print('\nRemovendo o ultimo elemento com o método pop()')
num.pop() # Método também usado para apagar um elemento de uma lista por indice se for informado, caso não seja ele sempre apaga o ultimo elemento da lista.

print('\nRemovendo um valor 1 com o método pop(1)')
num.pop(1)

print('\nRemovendo o valor 5 com o método remoce(5)')
num.remove(5) # Elimina atravês do valor/elemento informado eleminado sempre a primeira ocorrencia.

print(f'\nLista atual:')
for i, n in enumerate(num):
    print(f'Na posição {i}, encontrei o valor: {n}')

'''
OBS: criar uma variavel e atribuir o valor dela a outra variavel cria uma ligação entre ambas, tudo que for modificado em uma será modificado em outra
    Exemplo: 
        a = [1, 2, 3, 4, 5]
        b = a
Para contornar isso preciamos cria uma copia:
    Exemplo:
        a = [1, 2, 3, 4, 5]
        b = a[:]

'''

'''
Adicionando coleta de valores por input usando um laço de repetição

valores: [] -> Lista vazia
for cont in range(0, 5):
    valores.append(int(input('Digite um valor: ')))

print(valores)
'''