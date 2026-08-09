#Verificando a Unidade, Dezena, Centena e Milhar em um numero...

num = int(input('Digite um número: '))
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10
print('O número {}, tem:'.format(num))
print('Unidades: {}'.format(u))
print('Dezenas: {}'.format(d))
print('Centena: {}'.format(c))
print('Milhar: {}'.format(m))
