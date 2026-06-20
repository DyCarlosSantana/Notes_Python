# Desafio 17
"""
    Desafio 17: Etiqueta de Preço de Produtos
    O que fazer: Crie uma classe chamada Produto para gerenciar itens de uma loja.
    A classe deve receber o nome e o preco do produto no momento da criação.
    Crie um método chamado etiqueta_preco() que imprima uma etiqueta visualmente organizada com o nome do produto e o seu respectivo preço formatado.
"""
from rich.panel import Panel
class Produto:
    def __init__(self, produto, preco):
        self.produto = produto
        self.preco = preco

    def etiqueta_preco(self):
        etiqueta = Panel("Conteudo", title="Produto")
        return etiqueta

p1 = Produto("Iphone 15 Pro Max", 5000)
print(p1.etiqueta_preco())
