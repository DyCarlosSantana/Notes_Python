# Desafio 26
from abc import ABC, abstractmethod
from rich.panel import Panel
from rich.console import Console


class Funcionario(ABC):
    console = Console()
    def __init__(self, nome):
        self.nome = nome
        self.salario_bruto = 0
        self.salario_liquido = 0
        self.salario_min = 1621.00
        self.inss = 7.5

    @abstractmethod
    def calcular_salario_liquido(self):
        pass


    def analisar_salario(self):
        base = self.salario_liquido / self.salario_min
        conteudo = f"O salario de [blue]{self.nome}[/] ({self.__class__.__name__}) é de [green]R${self.salario_liquido:.2f}[/] e corresponde a [yellow]{base:.1f} salarios mínimos[/]."
        painel = Panel.fit(conteudo, title="Análise de Sálario", width=60)

        Funcionario.console.print(painel)


class FuncionarioHorista(Funcionario):
    def __init__(self, nome, valor_horas = 7.37, qtd_horas = 220):
        super().__init__(nome)
        self.valor_horas = valor_horas
        self.qtd_horas = qtd_horas
        self.salario_bruto = self.valor_horas * self.qtd_horas
    
    def calcular_salario_liquido(self):
        self.salario_liquido = self.salario_bruto - ((self.salario_bruto * self.inss) / 100)
        return self.salario_liquido


class FuncionarioMensalista(Funcionario):
    def __init__(self, nome, salario_bruto):
        super().__init__(nome)
        self.salario_bruto = salario_bruto

    def calcular_salario_liquido(self):
        valor_desconto = (self.salario_bruto * self.inss) / 100
        self.salario_liquido = self.salario_bruto - valor_desconto
        return self.salario_liquido