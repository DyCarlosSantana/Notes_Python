# Este é o arquivo número 97
"""
Exercício 97: Um print especial
O que fazer: Faça um programa que tenha uma função chamada escreva(), que receba um texto qualquer como parâmetro e mostre uma mensagem com tamanho adaptável.
Ex: escreva('Olá, Mundo!')
Resultado:
 Olá, Mundo!
"""
def escreva(msg):
    tam = len(msg) + 8
    print('-'* tam)
    print(f'    {msg}    ')
    print('-'* tam)

escreva('Ola, Mundo!')
escreva('Uma titulo grande!')