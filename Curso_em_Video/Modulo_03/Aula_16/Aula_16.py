# TUPLAS

lanche = ('Hambúrguer', 'Suco', 'Pizza', 'Pudim') #Parenteses são opcionais
'''
print(lanche)
print(lanche[1])
print(lanche[-1])
print(lanche[1:3]) #exibe o elemento 1 até o elemento 3 (mas não exibe o ultimo elemento, 3)
'''

i = 1
for comida in lanche:
    print(f'{i}.{comida}')
    i += 1
print(f'Quantidade de lanches pedidos: {len(lanche)}')


# Ou usar o enumerate:
for indice, comida in enumerate(lanche):
    print(f'{indice}.{comida}')
print(f'Quantidade de lanches pedidos: {len(lanche)}') # len() faz a leitura do comprimento/quantidade de componentes dentro de um objeto


for cont in range(0, len(lanche)):
    print(cont)

print(sorted(lanche)) # sorted() é usado para retornar uma lista ordenada

# Além do len() temos outros metodos
a = (2, 5, 4)
b = (5, 8, 1, 2)
c = b + a # Junta as duas tuplas, resultado (5, 8, 1, 2, 2, 5, 4)

print(c.count(5)) # count() irá contar quantas vezes o número 5 se repete em c;
print(c.index(8)) # index() verifica e retorna a posição do número 8 (em caso de números/elementos repetidos ele sempre pega a posição do primeiro);

# Diferente de algumas outras linguagens uma unica tuplas em Python pode armazenar varios tipos de dados diferentes.
pessoa = ('Carlos', 22, 'M', 95.50)

'''
Lista de Exercicios
    72 - Crie um programa que tenha uma tupla totalmente preenchida com uma contagem por extenso, e zero até vinte. Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostra-lo por entenso;
    
    73 - Crie uma tupla preenchida com os vinte primeiros colocados da tabela do comapeonato brasileiro de futebol, na ordem de colocação. Depois mostre:
        a) Apenas os 5 primeiros colocados;
        b) Os últimos 4 colocados da tabela;
        c) Uma lista com os times em ordem alfabetica;
        d) Em que posição na tabela o time da Chapecoense.
    
    74 - Crie um programa que irá gerar 5 números aleatorios e colocar em uma tupla. Depois disso, mostre a listagem de números gerados e também indique o menor e o maior valor que estão na tupla

    75 - Desenvolva um programa que leia 4 valores no teclado e seja colocado em uma tupla. No final, mostre:
        a) Quantas vezes aparece o valor 9;
        b)Em que posição foi digitado o primeiro valor 3
        C) Quais foram os números pares

    76 - Crie programa que tenha uma tupla unica com nomes de produtos e seus respectivos preçõs na sequencia. No final, mostre uma listagem de preçõs organizados em forma tabular.

    77 - Crie um programa que tenha uma tupla com varias palavras (não usar acentos). Depois disso, você deve mostrar, para cada palavra quais são as suas vogais.

'''
