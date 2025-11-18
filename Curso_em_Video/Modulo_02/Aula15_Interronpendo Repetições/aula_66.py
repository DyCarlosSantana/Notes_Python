# Desafio 66: Vários Números com Flag
# Objetivo:
# Ler vários números inteiros pelo teclado.
# O programa só deve parar quando o usuário digitar 999.
# No final, mostrar:
# Quantos números foram digitados.
# A soma entre eles (desconsiderando o 999).
cont = soma = 0
print('[Digite 999 para PARAR]')
while True:
    num = int(input('Digite um número: '))
    if num == 999:
        break
    cont += 1
    soma += num
print(f'A soma dos {cont} valores digitados é: {soma}')
