#Faça um programa que leia um ângulo qualquer e motre na tela o valor do seno, cosseno e tangente desse ângulo.
import math

angulo = float(input('Digite o anguulo que deseja: '))
seno = math.sin(math.radians(angulo))
cosseno = math.cos(math.radians(angulo))
tangente = math.tan(math.radians(angulo))
print('O ângulo de {}° tem o seno de: {:.2f}'.format(angulo, seno))
print('O ângulo de {}° tem o cosseno de: {:.2f}'.format(angulo, cosseno))
print('O ângulo de {}° tem a tangente de: {:.2f}'.format(angulo, tangente))