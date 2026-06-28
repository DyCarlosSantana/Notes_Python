from classesAvaliacao import AvaliacaoIMC, AvaliacaoMassaMagra
"""
    Script de teste para as classes AvaliacaoIMC e AvaliacaoMassaMagra.
    Cria instâncias de AvaliacaoIMC e AvaliacaoMassaMagra com dados de teste e exibe os resultados das avaliações físicas.
"""
lista_teste = [
    AvaliacaoIMC("2024-06-01", "Elisabeth", 48, 90, 1.70),
    AvaliacaoMassaMagra("2024-06-01", "Carlos", 46, 120, 1.70, 45),
    AvaliacaoIMC("2024-06-02", "Bruna", 14, 61, 1.63)
]

if __name__ == "__main__":
    for avaliacao in lista_teste:
        print(avaliacao.resumo())
        print(avaliacao.gerar_resultado())
        print("-" * 40)  # Separador entre avaliações
