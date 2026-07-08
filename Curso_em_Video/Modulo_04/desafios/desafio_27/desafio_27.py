# Desafio 25
from abc import ABC, abstractmethod
from rich.console import Console
from random import randint, choice
class Personagem(ABC):
    console = Console()
    def __init__(self, nome, vida):
        self.nome = nome
        self.vida = vida
        self.golpe = "Golpe"

    def atacar(self, alvo):
        forca = 100
        print(f"[magenta]{self.nome}[/]([cyan]{self.vida}[/]) atacou [yellow]{alvo}()[/] com [blue]{self.golpe}[/] de força [cyan]{forca}[/]")
        self.receber_dano(forca)

    def receber_dano(self, dano):
        self.vida -= dano
        print(f"[blue]{self.nome}[/] recebeu [red]dano de {dano}[/]!")

    @abstractmethod
    def curar(self):
        pass

# ----- Classes Filhas -----
class Guerreiro(Personagem):
    ataques_guerreiro = [
        "Ataque de Machado",
        "Pulo Giratório",
        "Arremeço de Machado",
        "Punho de Aço"
    ]
    def __init__(self, nome, vida):
        super().__init__(nome, vida)
        self.golpe = choice(Guerreiro.ataques_guerreiro)

    def curar(self):
        pontos_cura = randint(30, 100)
        print(f"{self.nome} tomou uma porção de cura de nivel 1 e [green]recuperou {pontos_cura} pontos[/] de vida")
    

class Mago(Personagem):
    ataques_mago = [
        "Feitiço de Congelamento",
        "Vórtice de Vento",
        "Magia de Envenenamento",
        "Conjuramento de Raios"
    ]
    def __init__(self, nome, vida):
        super().__init__(nome, vida)
        self.golpe = choice(Mago.ataques_mago)

    def curar(self):
        pontos_cura = randint(30, 100)
        print(f"{self.nome} usou mágia de cura e [green]recuperou {pontos_cura} pontos[/] de vida")