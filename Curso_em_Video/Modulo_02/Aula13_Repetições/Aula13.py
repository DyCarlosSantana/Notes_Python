# for c in range(0,10): #range = intervalo
#     print(c)
# print('_'*15)
# print('fim')

# for c in range(1,11):
#     print(c)
# print('_'*15)
# print('fim')

# for c in range(0,10):
#     print(c)
# print('_'*15)
# print('fim')

# for c in range(11,1, -1): #inverção de posição
#     print(c)
# print('_'*15)
# print('fim')

# for c in range(1,11, 2): #pula de 2 em 2
#     print(c)
# print('_'*15)
# print('fim')

n = int(input('Digite um numero: '))
for c in range(0, n+1):
    print(c)
print('_'*15)
print('fim')

i = int(input('Inicio: '))
f = int(input('Fim: '))
p = int(input('Passo: '))
for c in range(i, f+1, p):
    print(c)
print('_'*15)
print('fim')

s = 0
for c in range(0,3):
    n = int(input('Digite um número: '))
    s += n      #igual a (s = s + n)
print('Os três valores somados resulta em: {}'.format(s))