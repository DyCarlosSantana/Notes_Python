class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        
    def fazer_aniversario(self):
        self.idade += 1
    
"""
    Em Python, super().__init__() é usado dentro do construtor de uma classe filha para chamar o construtor ( __init__) de sua classe mãe. Isso garante que a classe filha herde e inicialize todas as variáveis ​​e configurações definidas na classe mãe sem reescrever o código.
"""

class Aluno(Pessoa):
    def __init__(self, nome, idade, curso, turma):
        super().__init__(nome, idade) 
        self.curso = curso
        self.turma = turma
    
    def fazer_matricula(self):
        pass


class Professor(Pessoa):
    def __init__(self, nome, idade, especialidade, nivel):
        super().__init__(nome, idade)
        self.especialidade = especialidade
        self.nivel = nivel

    def dar_aula(self):
        pass


class Funcionario(Pessoa):
    def __init__(self, nome, idade, cargo, setor):
        super().__init__(nome, idade)
        self.cargo = cargo
        self.setor = setor

    def bater_ponto(self):
        pass
