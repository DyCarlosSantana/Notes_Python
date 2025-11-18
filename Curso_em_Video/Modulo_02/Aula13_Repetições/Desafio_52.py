#Faça um programa que leia um número inteiro e diga se ele é ou não um número primo (divisiveis apenas por 1 ou por ele mesmo).

print('VERIFIQUE SE O NÚMERO É UM NÚMERO PRIMO')
print('')

# num = int(input("Digite um número inteiro: "))
# total_divisores = 0

# for i in range(1, num + 1):
#     if num % i == 0:
#         total_divisores += 1
# # Se for divisível apenas por 1 e por ele mesmo, é primo
# if total_divisores == 2:
#     print(f"O número {num} é PRIMO!")
# else:
#     print(f"O número {num} NÃO é primo!")

num = int(input('Digite um número: '))
total = 0
for c in range(1, num + 1):
    if num % c == 0:
        print('\033[34m', end='')
        total += 1
    else:
        print('\033[31m', end='')
    print('{}'.format(c), end=(' '))
print('\n\033[mO número {} foi divisivel {} vezes'.format(num, total))
if total == 2:
    print('Por isso ele é Primo.')
else:
    print('Por isso ele não é primo.')

