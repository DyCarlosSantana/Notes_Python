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

    def __init__(self, produto, preco):
        self.produto = produto
        self.preco = preco

    def linha(self, tam=30):
        return "-" * tam
    
    def conteudo(self, variavel_texto):
        justify_text = f"{variavel_texto:^30}"
        return justify_text
    
    def etiqueta_preco(self):
        etiqueta = Panel.fit(
            f"{self.conteudo(self.produto)}\n"
            f"{self.linha()}\n"
            f"{self.conteudo(f'R${self.preco}')}",
            title="Produto"
            )
        self.console.print(etiqueta)

p1 = Produto("Iphone 15 Pro Max", 5000)
print(p1.etiqueta_preco())
