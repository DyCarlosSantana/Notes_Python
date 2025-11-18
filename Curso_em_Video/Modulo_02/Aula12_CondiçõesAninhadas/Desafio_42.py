#Refaça o desafio (035) dos triangulos, acresecentando  recurso de mostrar que tipo de triangulo será formado
# Equilatero - todos os lados iguais
# Isósceles - dois lados iguais
# Escaleno - todos os lados diferentes
r1 = float(input('Primeiro Segmento:'))
r2 = float(input('Segundo Segmento:'))
r3 = float(input('Terceiro Segmento:'))

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os seguintes segmentos podem formae um triângulo, ', end=(''))
    if r1 == r2 == r3:
        print('EQUILATERO!')
    elif r1 != r2 != r3 != r1:
        print('ESCALENO!')
    else:
        print('ISÓCELES!')
else:
    print('Os segmentos podem formar um triângulo.')

# if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
#     print('Os Segmentos podem formar um triangulo!')
# else:
#     print('Os Segmentos não podem formar um triangulo!')