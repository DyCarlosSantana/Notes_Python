#Escreva um programa que leia um número inteiro qualquer e peça para o usuario esoclher qual será a base de conversão.
# - 1 para binario - 2 para octal - 3 hexadecimal.

n = int(input('Digite um número inteiro: '))
print('Escolha uma das bases para conversão: ')
print('[1] Converter para BINÁRIO')
print('[2] Converter para OCTAL')
print('[3] Converter para HEXADECIMAL')
opcao = int(input('Sua opção: ')) 
if opcao == 1:
    print('{} convertido para BINARIO é igual a {}.'.format(n, bin(n)[2:]))
elif opcao == 2:
    print('{} convertido para OCTAL é igual a {}.'.format(n, oct(n)[2:]))
elif opcao == 3:
    print('{} convertido para HEXADECIMAL é igual a {}.'.format(n, hex(n)[2:]))
else:
    print('Opção invalido. Tente novamente')