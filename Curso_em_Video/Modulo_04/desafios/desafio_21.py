# Desafio 21
"""
    Desafio 21: A Caneta Colorida Inteligente
    O que fazer: Crie uma classe chamada Caneta que interaja de forma rica com o terminal.
    O construtor deve inicializar a cor (que pode ser uma cor correspondente ao terminal) e o atributo tampada (que começa como True).
    Crie os métodos tampar() e destampar().
    Crie um método escrever(mensagem). Se a caneta estiver tampada, o sistema deve impedir a escrita. Se estiver destampada, deve imprimir a mensagem no terminal usando exatamente a cor da caneta.
    Crie um método quebrar_linha(qtd) que insira quebras de linha controladas.
"""
from rich import print
# from rich.console import Console
from rich.traceback import install
install()

class Caneta:
    cores_caneta = [
        "red",
        "green",
        "blue",
        "yellow",
        "magenta",
        "cyan",
        "white",
        "black"
    ]

    def __init__(self, cor="magenta"):
        cor_escolhida = cor.lower()
        if cor_escolhida not in self.cores_caneta:
            print(f"Cor '{cor}' não suportada. Definindo cor padrão (magenta).")
            self.cor = "magenta"
        else:
            self.cor = cor_escolhida
            self.tampada = True
    
    def tampar(self):
        self.tampada = True
        print("A caneta foi [magenta]Tampada[/].")

    def destampar(self):
        self.tampada = False
        print("A caneta foi [magenta]Destampada[/].")

    def escrever(self, texto:str):
        try:
            if self.tampada:
                print("Não é possivel escrever, caneta tampada")
            else:
                print(f"[{self.cor}]{texto}[/]")
        except (ValueError, TypeError) as erro:
            print(f"Erro: {erro.__class__}")
        
    def quebra_linha(self, qtd):
        print("\n" * qtd, end="")

caneta = Caneta("yellow")
caneta.destampar()
caneta.escrever("Alguma coisa em amarelo")
caneta.tampar()
caneta.escrever("tentando escrever com a caneta tamapada")
caneta = Caneta("orange") # Teste com uma cor invalida
caneta.quebra_linha(1)
caneta = Caneta("cyan")
caneta.destampar()
caneta.escrever("Texto na cor 'cyan após quebra de linha")