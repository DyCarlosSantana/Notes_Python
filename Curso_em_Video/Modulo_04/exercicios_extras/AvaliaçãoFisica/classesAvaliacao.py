from abc import ABC, abstractmethod

class AvaliacaoFisica(ABC):
    def __init__(self, data_avaliacao, nome, idade, peso, altura):
        self.data_avaliacao = data_avaliacao
        self.nome = nome
        self.idade = idade
        self.peso = peso
        self.altura = altura

    def resumo(self):
        """
        Retorna um resumo da avaliação física, incluindo data, nome, idade, peso e altura.
        """
        return f"Data da Avaliação: {self.data_avaliacao}\nNome: {self.nome}\nIdade: {self.idade}\nPeso: {self.peso} kg\nAltura: {self.altura}m"

    @abstractmethod
    def gerar_resultado(self):
        pass


class AvaliacaoIMC(AvaliacaoFisica):
    def __init__(self, data_avaliacao, nome, idade, peso, altura):
        super().__init__(data_avaliacao, nome, idade, peso, altura)

    def gerar_resultado(self):
        """
        Calcula o Índice de Massa Corporal (IMC) para ADULTOS (19 a 59 anos), e retorna a classificação correspondente.
        Abaixo do peso: Abaixo de 18,5
        Peso normal: Entre 18,5 e 24,9
        Sobrepeso: Entre 25 e 29,9
        Obesidade Grau I: Entre 30 e 34,9
        Obesidade Grau II: Entre 35 e 39,9
        Obesidade Grau III (Mórbida): Maior que 40
        """
        imc = self.peso / (self.altura ** 2)
        if imc < 18.5:
            classificacao = "Abaixo do peso"
        elif imc < 25:
            classificacao = "Peso normal"
        elif imc < 30:
            classificacao = "Sobrepeso"
        elif imc < 35:
            classificacao = "Obesidade Grau I"
        elif imc < 40:
            classificacao = "Obesidade Grau II"
        else:
            classificacao = "Obesidade Grau III (Mórbida)"

        return f"IMC: {imc:.2f} - Classificação: {classificacao}"


class AvaliacaoIMCIdoso(AvaliacaoFisica):
    def __init__(self, data_avaliacao, nome, idade, peso, altura):
        super().__init__(data_avaliacao, nome, idade, peso, altura)

    def gerar_resultado(self):
        """
        Calcula o Índice de Massa Corporal (IMC) para "IDOSOS" (a partir dos 60 anos), e retorna a classificação correspondente.
        Abaixo de 22: Baixo peso
        Entre 22 e 27: Peso adequado
        Acima de 27: Sobrepeso / Obesidade .
        """
        imc = self.peso / (self.altura ** 2)
        if imc < 22:
            classificacao = "Abaixo do peso"
        elif imc < 27:
            classificacao = "Peso normal"
        else:
            classificacao = "Sobrepeso / Obesidade"

        return f"IMC: {imc:.2f} - Classificação: {classificacao}" 


class AvaliacaoMassaMagra(AvaliacaoFisica):
    def __init__(self, data_avaliacao, nome, idade, peso, altura, percentual_gordura):
        super().__init__(data_avaliacao, nome, idade, peso, altura)
        self.percentual_gordura = percentual_gordura

    def gerar_resultado(self):
        """
        Calcula a Massa Magra com base no peso e percentual de gordura corporal.
        """
        massa_magra = self.peso * (1 - (self.percentual_gordura / 100))
        return f"Massa Magra: {massa_magra:.2f} kg - Percentual de Gordura Corporal: {self.percentual_gordura:.2f}%"
    