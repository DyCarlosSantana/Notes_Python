# Desafio 18
"""
    Desafio 18: Planejador de Churrasco
    O que fazer: Crie uma classe chamada Churrasco para calcular a logística de comida de um evento.
    A classe deve ter um atributo de classe chamado consumo_padrao (por exemplo, 400g de carne por pessoa).
    O construtor deve registrar a quantidade de pessoas convidadas.
    Crie um método chamado analisar() que calcule a quantidade total de carne necessária para o evento
    e exiba um resumo completo dos custos estimados.
"""
from rich.panel import Panel
from rich.traceback import install
install()
class Churrasco:
    consumo_padrao = 0.4
    preco_kg = 82.40

    def __init__(self, titulo, quant):
        self.titulo = titulo
        self.quant = quant

    def quant_carne(self):
        total_carne = self.consumo_padrao * self.quant
        return total_carne
    
    def total_custo(self):
        valor_total = self.quant_carne() * self.preco_kg
        return valor_total
    
    def valor_por_pessoa(self):
        valor_dividido = self.total_custo() / self.quant
        return valor_dividido

    def analisar(self):
        msg = Panel(f"Analisando {self.titulo} com {self.quant} pessoas\nCada participante comerá {self.consumo_padrao} e cada kg custa R${self.preco_kg}\nRecomendo comprar {self.quant_carne():.2f} kg de carne, o que custará R${self.total_custo():.2f}\nO valor por pessoa será de R${self.valor_por_pessoa():.2f}")
        return msg

churrasco = Churrasco("Churrasco dos Amigos", 10)
print(churrasco.analisar())