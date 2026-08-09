from desafio_26 import *


def main():
    f1 = FuncionarioHorista("Claudio")
    f1.calcular_salario_liquido()
    f1.analisar_salario()

    f2 = FuncionarioMensalista("Karolina", 6000)
    f2.calcular_salario_liquido()
    f2.analisar_salario()

if __name__ == "__main__":
    main()