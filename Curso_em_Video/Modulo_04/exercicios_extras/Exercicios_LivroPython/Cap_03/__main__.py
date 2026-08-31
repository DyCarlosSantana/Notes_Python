from exercicio import Exercicio, PlanoTreino


ex1 = Exercicio("Quadriceps", "Extensora", 4, 12)
ex2 = Exercicio("Quadriceps", "Agachamento", 3, 12)
ex3 = Exercicio.isometria("Abdomen", "Prancha", 90) # Usando @classmethod

ficha = PlanoTreino("Bruna", ex1)
ficha.adicionar_exercicio(ex2)
ficha.adicionar_exercicio(ex3)

def main():
    if __name__ == "__main__":
        ficha.exibir_ficha()
        ficha.classificar_imc(25.8) # Usando @staticmethod

main()