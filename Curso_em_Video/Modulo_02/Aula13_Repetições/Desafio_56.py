#Desenvolva um programa que leia o (nome, idade e sexo) de 4 pessoas. No final do programa, mostre:
#A media de idade do grupo
#Qual o nome do homem mais velo
#Quantas mulheres têm menos de 20 anos.
cont = 0
soma_idade = 0
homem_mais_velho = 0
nome_mais_velho = ''
mulheres_menos20 = 0
for p in range(1, 5):
    print(f'---------- {p}° PESSOA ----------')
    nome = str(input('NOME: ')).upper().strip()
    idade = int(input('IDADE: '))
    sexo = str(input('SEXO [M/F]: ')).upper().strip()
    soma_idade += idade #coleta e soma todas as idades para depois ser feita a média
    if sexo == 'M':
        if idade > homem_mais_velho: #Adicionar o nome e idade do homem mais velho do grupo
            homem_mais_velho = idade
            nome_mais_velho = nome
        elif sexo == 'M':
            if idade < 20: #Adicionar a quantidade de mulheres com menos de 20 anos
                mulheres_menos20 += 1 
    cont += 1
    media_idade = soma_idade / cont #Calcular a media de idade do grupo

print(f'A média de idade do grupo é {media_idade}')
print(f'O homem mais velho tem {homem_mais_velho}, e se chama {nome_mais_velho}')
print(f'Ao todo são {mulheres_menos20} mulheres com menos de 20 anos')