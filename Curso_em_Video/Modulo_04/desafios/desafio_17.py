# Desafio 17
"""
    Desafio 17: Etiqueta de Preço de Produtos
    O que fazer: Crie uma classe chamada Produto para gerenciar itens de uma loja.
    A classe deve receber o nome e o preco do produto no momento da criação.
    Crie um método chamado etiqueta_preco() que imprima uma etiqueta visualmente organizada com o nome do produto e o seu respectivo preço formatado.
"""
from rich.console import Console
from rich.panel import Panel
from rich.traceback import install
install()

class Produto:
    console = Console()

    def __init__(self, produto:str, preco:float):
        self.produto = produto
        self.preco = preco

    def linha(self, tam=30):
        return "-" * tam
    
    def etiqueta_preco(self):
        conteudo = f"{self.produto.center(30, ' ')}\n"
        conteudo += f"{self.linha()}\n"
        # formatando o preço
        precof = f"R${self.preco:,.2f}"
        conteudo += f"{precof.center(30, '.')}"
        etiqueta = Panel.fit(conteudo, title="Produto")
        self.console.print(etiqueta)

p1 = Produto("Iphone 15 Pro Max", 5_000.00)
p1.etiqueta_preco()
