from rich import inspect
from classes_exercicio_04 import Aluno, Professor, Funcionario

a1 = Aluno("Carlos", 22, 20230790341, "ADS2023")
inspect(a1, methods=True)

p1 = Professor("João", 46, "Banco de Dados", "Mestrado")
inspect(p1, methods=True)

f1 = Funcionario("Julia", 30, "Secretaria", "Secreatariado")
inspect(f1, methods=True)