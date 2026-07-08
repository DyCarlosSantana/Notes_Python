from desafio_27 import *

def main():
    p1 = Guerreiro("Kratos", 1800)
    p2 = Mago("Merlin", 2000)

    p1.atacar(p2)
    p2.atacar(p1)

    p1.curar()
    p2.curar


if __name__ == "__main__":
    main()