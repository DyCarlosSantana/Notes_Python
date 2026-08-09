"""
Exercício 112: Entrada de Dados Monetários
O que fazer: Dentro do pacote utilidadesCeV que criou no desafio 111, temos um subpacote chamado dado. Crie uma função chamada leiaDinheiro() que seja capaz de funcionar como a função input(), mas com uma validação de dados para aceitar apenas valores que sejam monetários (substituindo vírgula por ponto).
"""

def leiaDinheiro(msg):
    valido = False
    while not valido:
        entrada = str(input(msg)).replace(',', '.').strip()
        if entrada.isalpha() or entrada == '':
            print(f'O preço "{entrada}" é invalido!')
        else:
            valido = True
            return float(entrada)
