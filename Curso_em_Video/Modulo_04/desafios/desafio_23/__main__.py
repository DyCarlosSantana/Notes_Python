from desafio_23 import Quadrado, Circulo

q = Quadrado(12)
c = Circulo(50)

if __name__ == "__main__":
    print('-----' * 5)
    print(f"Perimetro do Quadrado: {q.calcular_perimetro():.2f} cm")
    print(f"Área do Quadrado: {q.calcular_area():.2f} cm")
    print('-----' * 5)
    print(f"Perimetro do Circulo: {c.calcular_perimetro():.2f} cm")
    print(f"Área do Circulo: {c.calcular_area():.2f} cm")
    print('-----' * 5)