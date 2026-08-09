# Desafio 16
"""
    Desafio 16: Classe Funcionário (Introdução)
    O que fazer: Crie uma classe chamada Funcionario que represente um colaborador de uma empresa.
    O construtor deve inicializar os atributos de instância: nome, setor e cargo.
    Instancie pelo menos dois funcionários diferentes e mostre os seus dados na tela.
"""
from rich import print

class Funcionario:
    # Atributo de Classe
    empresa = "Drip Art"
    def __init__(self, nome, cargo, setor):
        self.nome = nome
        self.cargo = cargo
        self.setor = setor
    
    def apresentacao(self):
        msg = (f":wave::grin: Olá, sou [blue]{self.nome}[/], {self.cargo} do setor de {self.setor} da empresa {Funcionario.empresa}") #  OU {self.__class__.empresa}
        return msg

f1 = Funcionario("Edy Carlos", "programador", "TI" )
print(f1.Apresentaçao())