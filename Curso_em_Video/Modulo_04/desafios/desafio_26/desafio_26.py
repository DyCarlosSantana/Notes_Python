# Desafio 26
from abc import ABC, abstractmethod

class Funcionario(ABC):
    def __init__(self, nome, salario_bruto, salario_liquido):
        self.nome = nome
        self.salario_bruto = salario_bruto
        self.salario_liquido = salario_liquido
        self.salario_min = 1621.00
        self.inss - 7.5

    @abstractmethod
    def calcular_salario_liquido(self):
        pass

    def analisar_salario(self):
        pass # função concreta