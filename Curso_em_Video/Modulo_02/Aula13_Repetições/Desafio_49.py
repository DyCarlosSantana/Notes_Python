#Refaça o Desafio 09, mostrando a tabuada de um número que o usuario escolher, so que agora utilizando um laço (for)
print('{:=^50}'.format('TABUADA'))
n = int(input('Você gostaria de ver a tabuada de qual número: '))
print('ADIÇÃO')
for c in range(1, 11):
    print('{} + {} = {}'.format(n, c, (n+c)))
print('_'*15)

print('SUBTRAÇÃO')
for c in range(1, 11):
    print('{} - {} = {}'.format(n, c, (n-c)))
print('_'*15)

print('MULTIPLICAÇÃO')    
for c in range(1, 11):
    print('{} x {} = {}'.format(n, c, (n*c)))
print('_'*15)

print('DIVISÃO')    
for c in range(1, 11):
    print('{} % {} = {:.1f}'.format(n, c, (n/c)))

print('_'*15)
print('Fim')