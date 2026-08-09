# Desafio 33: Faça um programa que leia três números e mostre qual é o maior e qual é o menor.

n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))    
n3 = int(input('Digite o terceiro número: '))

# (TESTE) - print('O maior valor é {}.'.format(max(n1, n2, n3)))

# Verificando quem é o menor
menor = n1
if n2 < n1 and n2 < n3:
    menor = n2
elif n3 < n1 and n3 < n2:
    menor = n3
# Verificando quem é o maior
maior = n1
if n2 > n1 and n2 > n3:
    maior = n2
elif n3 > n1 and n3 > n2:
    maior = n3

print(f'O menor número é {menor}')
print(f'O maior número é {maior}')
print('Fim do programa')


'''
if n1 > n2 and n1 > n3:
    print(f'O maior número é {n1}')
if n2 > n1 and n2 > n3:
    print(f'O maior número é {n2}')
if n3 > n1 and n3 > n2:
    print(f'O maior número é {n3}')
if n1 < n2 and n1 < n3:
    print(f'O menor número é {n1}') 
if n2 < n1 and n2 < n3:
    print(f'O menor número é {n2}')
if n3 < n1 and n3 < n2:
    print(f'O menor número é {n3}')
print('Fim do programa')
'''