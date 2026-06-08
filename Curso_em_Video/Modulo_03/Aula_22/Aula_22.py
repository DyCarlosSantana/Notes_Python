num = int(input('Digite um número: '))
def fatorial(num):
    f = 1
    for c in range(1, num+1):
        f*= c
    return f
fat = fatorial(num)
print(f'O fatorial de {num} é {fat}')