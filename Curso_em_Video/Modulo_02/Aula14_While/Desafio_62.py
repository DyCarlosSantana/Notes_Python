#Melhore o desafio 61, perguntando para o usuario se ele quer mostrar mais alguns termos. O programa encerra quando ele disser não quer mostrar os termos.

print('='*20)
print('10 PRIMEIROS TERMOS')
print('='*20)

primeiro_termo = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
termo = primeiro_termo
cont = 1
total_termos = 0
mais = 10
while mais != 0:
    total_termos = total_termos + mais
    while cont <= 10:
        print('{} -> '.format(termo),end='') 
        termo += razao
        cont += 1
    print('PAUSA') 
    mais = int(input('Gostaria de ver mais quantos termos?: '))
print(f'Progressão finalizada com {total_termos} termos mostrados.')