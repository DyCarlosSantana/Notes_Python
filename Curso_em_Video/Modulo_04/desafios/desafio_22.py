# Desafio 22
"""
    Desafio 22: O Simulador de Controle Remoto
    O que fazer: Crie uma classe chamada ControleRemoto que gerencie os comandos de uma televisão.
    Defina atributos para controlar o canal_atual, o volume_atual e o limite de volume (por exemplo, volume máximo = 5).
    Crie métodos comportamentais para subir e descer o volume (respeitando os limites mínimos e máximos) e mudar de canal (para cima ou para baixo).
    Implemente um método de controle principal que receba comandos do usuário (como símbolos ou números) no terminal e acione os métodos correspondentes da televisão.
"""
from rich.panel import Panel
from rich.console import Console
from rich.traceback import install
install()

class ControleRemoto:
    canal_min = 1
    canal_max = 5
    volume_min = 1
    volume_max = 10
    console = Console()

    def __init__(self, canal, volume):
        self.canal_atual = canal
        self.volume_atual = volume
        self.ligado:bool = False

    def liga_desliga(self):
        self.ligado = not self.ligado

    def canal_mais(self):
        if self.ligado:
            if self.canal_atual == ControleRemoto.canal_max:
                self.canal_atual = ControleRemoto.canal_min
            else:
                self.canal_atual += 1
        
    def canal_menos(self):
        if self.ligado:
            if self.canal_atual == ControleRemoto.canal_min:
                self.canal_atual = ControleRemoto.canal_max
            else:
                self.canal_atual -= 1

    def volume_mais(self):
        if self.ligado:
            if self.volume_atual != ControleRemoto.volume_max:
                self.volume_atual += 1


    def volume_menos(self):
        if self.ligado:
            if self.volume_atual != ControleRemoto.volume_min:
                self.volume_atual -= 1

    def mostrar_controle(self):
        conteudo = f"\n  [bold]<[/] CHA [bold]>[/]   |   [bold]+[/] VOL [bold]-[/]  "
        controle = Panel.fit(conteudo, title="[ CONTROLE ]")
        self.console.print(controle)

    def mostrar_tv(self):
        if not self.ligado:
            conteudo = "[red]TV Desligada[/]"
        else:
            conteudo = "CANAL: "
            for canal in range(ControleRemoto.canal_min, ControleRemoto.canal_max +1):
                if canal == self.canal_atual:
                    conteudo += f" [blue on yellow] {canal} [/] "
                else:
                    conteudo += f" {canal} "

            conteudo += f"\n\nVOLUME: "
            for volume in range(ControleRemoto.volume_min, ControleRemoto.volume_max +1):
                if volume <= self.volume_atual:
                    conteudo += f"[yellow on yellow]  [/]"
                else:
                    conteudo += f"[blue on blue]  [/]"
            conteudo += f"  {self.volume_atual}"

        painel_tv = Panel(conteudo, title="[ TV ]", width=40)

        self.console.print(painel_tv)

controle = ControleRemoto(2, 5)

while True:
    controle.mostrar_tv()
    controle.mostrar_controle()
    comando = str(input("COMANDO: "))
    match comando:
        case 0:
            break
        case "@":
            controle.liga_desliga()
        case "+":
            controle.volume_mais()
        case "-":
            controle.volume_menos()
        case ">":
            controle.canal_mais()
        case "<":
            controle.canal_menos()

    print(f"\n" * 5)
