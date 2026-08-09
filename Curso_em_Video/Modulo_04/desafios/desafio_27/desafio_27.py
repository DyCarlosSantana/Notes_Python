# Desafio 25
from abc import ABC, abstractmethod
from rich import print
from random import randint, choice

class Personagem(ABC):
    def __init__(self, nome, vida = 1500):
        self.nome = nome
        self.vida = vida
        self.golpe = []

    def atacar(self, alvo, forca = 100):
        print(f"[magenta]{self.nome}[/]([cyan]{self.vida}[/]) atacou [yellow]{alvo.nome}()[/] com [blue]{self.golpe}[/] de força [cyan]{forca}[/]")
        alvo.receber_dano(forca)

    def receber_dano(self, dano):
        fator = randint(5, dano)
        self.vida = self.vida - fator
        if self.vida < 0:
            self.vida = 0
            print(f"Gamer Over para {self.nome}!")
        else:
            print(f"[blue]{self.nome}[/] recebeu [red]dano de {fator}[/]!")

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
        self.vida += pontos_cura
        print(f"[magenta]{self.nome}[/] tomou uma porção de cura de nivel 1 e [green]recuperou {pontos_cura} pontos[/] de vida")
    

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
        self.vida += pontos_cura
        print(f"[magenta]{self.nome}[/] usou mágia de cura e [green]recuperou {pontos_cura} pontos[/] de vida")