# Desafio 26
from abc import ABC, abstractmethod
from rich.panel import Panel
from rich.console import Console


class Funcionario(ABC):
    console = Console()
    def __init__(self, nome, salario_bruto):
        self.nome = nome
        self.salario_bruto = salario_bruto
        self.salario_liquido = 0
        self.salario_min = 1621.00
        self.inss = 7.5

    @abstractmethod
    def calcular_salario_liquido(self):
        pass

    def analisar_salario(self):
        conteudo = f"O salario de [blue]{self.nome}[/] é de [green]R${self.salario_liquido}[/] e corresponde a [yellow](...) salarios mínimos[/]."
        painel = Panel(conteudo, title="Análise de Sálario")

        Funcionario.console.print(painel)


class FuncionarioHorista(Funcionario):
    def __init__(self, nome, valor_horas, qtd_horas):
        super().__init__(nome, salario_bruto = 0)
        self.valor_horas = valor_horas
        self.qtd_horas = qtd_horas
    
    def calcular_salario_liquido(self):
        self.salario_bruto = self.valor_horas * self.qtd_horas
        valor_desconto = (self.salario_bruto * self.inss) / 100
        self.salario_liquido = self.salario_bruto - valor_desconto
        return self.salario_liquido


class FuncionarioMensalista(Funcionario):
    def __init__(self, nome, salario_bruto):
        super().__init__(nome, salario_bruto)

    def calcular_salario_liquido(self):
        valor_desconto = (self.salario_bruto * self.inss) / 100
        self.salario_liquido = self.salario_bruto - valor_desconto
        return self.salario_liquido