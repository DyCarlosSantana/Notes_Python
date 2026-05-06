# Este é o arquivo número 94
#O que fazer: Crie um programa que leia nome, sexo e idade de várias pessoas, guardando os dados de cada pessoa num dicionário e todos os dicionários numa lista. No final, mostre:
# Quantas pessoas foram cadastradas.
# A média de idade.
# Uma lista com as mulheres
# Uma lista com as pessoas com idade acima da média.

cadastros = []
pessoa = {}

while True:
    pessoa['Nome'] = str(input('Nome completo: '))
    pessoa['Idade'] = int(input('Idade: '))
    pessoa['Sexo'] = str(input('Sexo [M/F]: ')).upper()
    cadastros.append(pessoa.copy())
    pessoa.clear()

    resp = input('Deseja continuar [S/N]').upper()
    if resp == 'N':
        break

print('==+=='*8)
print(cadastros)
print('==+=='*8)
print('')

idade = []
for i in cadastros:
    idade.append(i.get('Idade'))
media = sum(idade) / len(cadastros)

print(f'Foram cadastradas {len(cadastros)} pessoas;')
print(f'A média de idade é {media};')
print(f'As mulheres cadastradas são: ')
mulheres = []
for f in cadastros:
    if f['Sexo'] == 'F':
        mulheres.append(f.copy())
for i in mulheres:
    print(i.get('Nome'))

print('As pessoas com idade acima da média são:')
pessoa_acima_media = []
for p in cadastros:
    if p['Idade'] > media:
        pessoa_acima_media.append(p.copy())
for i in pessoa_acima_media:
    print(f'{i['Nome']} com {i['Idade']} anos de idade.')