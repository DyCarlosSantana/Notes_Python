# Declaração de Classes
class Gafanhoto:
    # Metodo construtor
    def __init__(self):
        # Atributos de instancia
        self.nome = ""
        self.idade = 0
        
    # Métodos de instancia
    def aniversario(self):
        self.idade += 1
    
    def mensagem(self):
        return f"{self.nome} é um gafanhoto e tem {self.idade} anos de idade."

# Declaração de Obejtos
g1 = Gafanhoto()
g1.nome = "Carlos"
g1.idade = 22
print(g1.mensagem())
