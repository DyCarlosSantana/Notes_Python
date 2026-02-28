"""
Exercício 84: Lista Composta e Análise de Dados
O que fazer: Faça um programa que leia o nome e o peso de várias pessoas, guardando tudo numa lista composta. No final, mostre:
Quantas pessoas foram cadastradas.
Uma listagem com as pessoas mais pesadas (mostre o peso e os nomes).
Uma listagem com as pessoas mais leves (mostre o peso e os nomes).
"""
cadastros = []
pessoa = []
mais_pesado = []
mais_leve = []

while True:
    try:
        nome = str(input("Nome: ")).strip()
        pessoa.append(nome)
        peso = int(input("Peso: "))
        pessoa.append(peso)
        cadastros.append(pessoa[:])
        pessoa.clear()

        print("Selecione uma opção: ")
        resp = int(input("[0] Encerrar Cadastro\n[1] Continuar Cadastro \n"))
        if resp == 0:
            break
        
    except:
        print("Dado invalido! Tente novamente...")


for pessoa in cadastros:
    if pessoa[1] > 70:
        mais_pesado.append(pessoa[:])
    else:
        mais_leve.append(pessoa[:])

print(f"Mais pesados são ", end='')
for mp in mais_pesado:
    print(f"{mp[0]} com {mp[1]}Kg... ", end='')

print(f"\nMais leve são ", end='')
for ml in mais_leve:
    print(f"{ml[0]} com {ml[1]}Kg... ", end='')

print(f"\nForam cadastradas {len(cadastros)} pessoas")
