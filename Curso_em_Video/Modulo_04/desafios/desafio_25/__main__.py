from desafio_25 import Caminhao, Moto, Drone
from rich.panel import Panel
from rich import print
# Atributos: Distancia e Frete

def main():
    dist = 30

    entrega = [Moto(dist), Drone(dist), Caminhao(dist)]
    for i in entrega:
        painel = Panel(
            f'[cyan]Frete de {dist}km:[/] [magenta]{i.calcular_frete()}[/]',
            width=40,
            title=f"{type(i).__name__}",
            border_style="cyan")
        print(painel)

if __name__ == "__main__":
    main()