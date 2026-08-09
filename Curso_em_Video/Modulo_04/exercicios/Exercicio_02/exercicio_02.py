"""
    Melhorando o exercicio 01 da Aula 04
"""

# Declaração de Classes
class Gafanhoto:
    # Metodo construtor
    def __init__(self, nome = "vazio", idade = 0): # Adiciona valores padrão, caso seja opcional.

        # Atributos de instancia
        self.nome = nome
        # recebe seus respectivos parametros
        self.idade = idade
        
    # Métodos de instancia
    def aniversario(self):
        self.idade += 1
    
    def mensagem(self):
        return f"{self.nome} é um gafanhoto(a) e tem {self.idade} anos de idade."

# Declaração de Obejtos
g1 = Gafanhoto("Carlos", 22)
print(g1.mensagem())

g2 = Gafanhoto("Bruna", 14)
print(g2.mensagem())