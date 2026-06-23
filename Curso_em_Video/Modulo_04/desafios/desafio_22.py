# Desafio 22
"""
    Desafio 22: O Simulador de Controle Remoto
    O que fazer: Crie uma classe chamada ControleRemoto que gerencie os comandos de uma televisão.
    Defina atributos para controlar o canal_atual, o volume_atual e o limite de volume (por exemplo, volume máximo = 5).
    Crie métodos comportamentais para subir e descer o volume (respeitando os limites mínimos e máximos) e mudar de canal (para cima ou para baixo).
    Implemente um método de controle principal que receba comandos do usuário (como símbolos ou números) no terminal e acione os métodos correspondentes da televisão.
"""

class ControleRemoto:
    volume_max = 5
    def __init__(self, canal_atual, volume_atual):
        self.canal_atual = canal_atual
        self.volume_atual = volume_atual
        