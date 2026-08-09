# Desafio 20
"""
    Desafio 20: Perfil Gamer com Jogos Favoritos
    O que fazer: Crie uma classe chamada Gamer que gerencie o perfil de um jogador.
    O construtor deve receber o nome e o nick (apelido do jogador).
    Adicione um atributo de instância que armazene múltiplos jogos favoritos (uma coleção como lista ou dicionário).
    Crie métodos para adicionar novos jogos a essa lista e exiba o perfil completo do jogador com os seus jogos favoritos organizados em ordem alfabética.
"""
from rich.console import Console
from rich.panel import Panel
from rich.traceback import install
install()

class Gamer:
    console = Console()
    def __init__(self, name, nickName):
        self.name = name
        self.nick = nickName
        self.lista_favoritos = []

    def linha(self, tam=40):
        return "-" * tam
    
    def add_favoritos(self, nome_jogo:str):
        try:
            self.lista_favoritos.append(nome_jogo.capitalize())
        except (ValueError, TypeError):
            return "Erro ao adicionar jogo em favoritos"
    
    def exibir_favs(self):
        favoritos_ordenados = sorted(self.lista_favoritos)
        return "\n".join(favoritos_ordenados)

    def perfil(self):  
        painel = Panel(
            f"Nome: {self.name}\n"
            f"[green]{self.linha()}[/]\n"
            f"[green]Marcados como Favoritos:[/]\n"
            f"{self.exibir_favs()}\n",
            title=f"Jogador - {self.nick}",
            title_align="left",
            border_style="green",
            expand=False
        )
        self.console.print(painel)
    
p1 = Gamer("Edy Carlos de Sanatana Souza", "DyCarlos26")
p1.add_favoritos("Minecraft")
p1.add_favoritos("Stardew Valley")
p1.add_favoritos("Magic Rampage")
p1.perfil()