from desafio_27 import *
from rich import inspect


def main():
    p1 = Guerreiro("Kratos", 1800)
    p2 = Mago("Merlin", 2000)

    p1.atacar(p2, 200)
    p2.atacar(p1)

    p1.curar()
    p2.curar()
    inspect(p1)
    inspect(p2)


if __name__ == "__main__":
    main()