# Exercício 96: Função que calcula área
# O que fazer: Faça um programa que tenha uma função chamada area(), que receba as dimensões de um terreno retangular (largura e comprimento) e mostre a área do terreno.

def cal_area(largura, comprimento):
    area = largura * comprimento
    print(f'A área de um terreno com ({largura} x {comprimento}) é de {area}m²')

largura = float(input('Insira a Largura do terreno: '))
comprimento = float(input('Insira o comprimento do terreno: '))
cal_area(largura, comprimento)