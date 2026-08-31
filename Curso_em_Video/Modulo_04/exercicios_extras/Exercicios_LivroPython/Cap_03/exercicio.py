
class Exercicio:
    def __init__(self, grupo_muscular, nome_exercicio, series, repeticoes):
        self.grupo_muscular = grupo_muscular
        self.nome =  nome_exercicio
        self.series = series
        self.rep = repeticoes
        
    @classmethod
    def isometria(cls, grupo_muscular, nome_exercicio, tempo_segundos):
        cls.grupo_muscular = grupo_muscular
        cls.nome = nome_exercicio
        cls.series = 1
        cls.rep = tempo_segundos
    
    def resumo(self):
        return f"{self.grupo_muscular}: {self.nome} - {self.series}x{self.rep}"


class PlanoTreino:
    def __init__(self, nome_atleta, exercicio):
        self.nome = nome_atleta
        self.exercicio = []
    
    @staticmethod
    def classificar_imc(imc):
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
            
        return f"Classificação: {classificacao}"
    
    def adicionar_exercicio(self, novo_exercicio):
        self.exercicio.append(novo_exercicio)
        
    def carga_total(self):
        pass
    
    def exibir_ficha(self):
        for index, i in enumerate(self.exercicio, 1):
            print(f"{index}. {i}")