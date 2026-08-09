# Desafio 23
"""
    Desafio 1 (23) — Polígonos e Abstração
    Conceitos centrais: Classe Abstrata + Métodos Abstratos

    Requisitos:
    Classe abstrata Poligono (usando ABC + @abstractmethod)
    Atributos genéricos na classe mãe (ex: quantidade de lados)
    Métodos abstratos: calcular_perimetro() e calcular_area()
    Subclasses concretas:
    Quadrado → recebe o comprimento do lado
    Circulo → recebe o raio
    Cada subclasse implementa sua própria fórmula de área e perímetro
    Testar instanciando objetos das duas subclasses
"""
from math import pi
from abc import ABC, abstractmethod

class Poligono(ABC):
    def __init__(self, lado):
        self.lado = lado
    
    @abstractmethod
    def calcular_perimetro(self):
        pass

    @abstractmethod
    def calcular_area(self):
        pass


class Quadrado(Poligono):
    def __init__(self, lado):
        super().__init__(lado)
        self.comprimento_lados = lado
    
    def calcular_perimetro(self):
        """
        Calcula o Perimetro do Quadrado
        Fórmula: P = 4 . l
        """
        perimetro = 4 * self.comprimento_lados
        return perimetro
    
    def calcular_area(self):
        """
        Calcula o a Área do Quadrado
        Fórmula: A = l²
        """
        area = self.comprimento_lados ** 2
        return area


class Circulo(Poligono):
    def __init__(self, lado):
        super().__init__(lado)
        self.raio = lado
    
    def calcular_perimetro(self):
        """
        Calcula o Perimetro do Circulo
        Fórmula: P = 2 . pi . r
        """
        perimetro = 2 * (pi * self.raio)
        return perimetro


    def calcular_area(self):
        """
        Calcula o Área do Circulo
        Fórmula: A = pi . r²
        """
        area = pi * (self.raio ** 2)
        return area