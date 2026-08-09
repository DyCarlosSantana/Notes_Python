#Desenvolva um programa que leia o primeiro e a razão de uma PA. No final, motre os 10 primeiros termos dessa progressão.
#PA = progressão Aritimetica
print('='*20)
print('10 PRIMEIROS TERMOS')
print('='*20)

primeiro_termo = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
decimo = primeiro_termo + (10 - 1) * razao #Formula para o Decimo termo de uma PA

for c in range(primeiro_termo, decimo + razao, razao):
    print('{}'.format(c),end=' -> ')
print('Acabou')