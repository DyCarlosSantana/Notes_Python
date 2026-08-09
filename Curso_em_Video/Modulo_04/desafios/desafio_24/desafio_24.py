# Desafio 24

from abc import ABC, abstractmethod

class BebidaQuente(ABC):
    def preparar(self):
        print("----- Iniciando Preparo -----")
        self.ferver_agua()
        self.misturar()
        self.servir()
        print("------- Bebida Pronta -------")

    def ferver_agua(self):
        print("1 - Fervendo a água a 100°")

    @abstractmethod
    def misturar(self):
        pass

    @abstractmethod
    def servir(self):
        pass


class Cafe(BebidaQuente):
    def misturar(self):
        print("2 - Passando aguá na borra de café ")

    def servir(self):
        print("3 - Servindo Café na Xicara")

class Cha(BebidaQuente):
    def misturar(self):
        print("2 - Colocando Sache de chá na aguá fervente")

    def servir(self):
        print("3 - Servindo Chá na Xicara")

class Leite(BebidaQuente):
    def misturar(self):
        print("2 - Passando aguá vervente e misturando ao leite")

    def servir(self):
        print("3 - Servindo Leite na Xicara")
    