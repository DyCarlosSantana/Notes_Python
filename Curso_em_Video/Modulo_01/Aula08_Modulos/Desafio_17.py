#Faça um programa que leia a comprimento do cateto oposto e do cateto adjacente de um triangulo, calcule e mostre o comprimento da hipotenusa.

#Metodo 01
co = float(input("Comprimento do cateto aposto: "))
ca = float(input("Comprimento do cateto adjacente: "))
hi = (co ** 2 + ca ** 2) ** (1/2)   #Forma matematica para calcular a hipotenusa.
print ("A hipotenusa vai medir {:.2f}".format(hi))

#Metodo 02
import math
co = float(input("Comprimento do cateto oposto: "))
ca = float(input("Comprimento do cateto adjacente: "))
hi = math.hypot(co, ca)   #Uso da função "hypot" do metodo "Math", para calcular a hipotenusa.
print ("A hipotenusa vai medir {}".format(math.trunc(hi)))