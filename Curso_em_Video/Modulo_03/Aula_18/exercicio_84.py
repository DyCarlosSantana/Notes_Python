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

        if len(cadastros) == 0:
            mais_pesado = mais_leve = pessoa[1]
        else:
            if pessoa[1] > mais_pesado:
                mais_pesado = pessoa[1]
            if pessoa[1] < mais_leve:
                mais_leve = pessoa[1]

        cadastros.append(pessoa[:])
        pessoa.clear()

        print("Selecione uma opção: ")
        resp = int(input("[0] Encerrar Cadastro\n[1] Continuar Cadastro \n"))
        if resp == 0:
            break
        
    except:
        print("Dado invalido! Tente novamente...")


print(f"O maior peso é {mais_pesado}kg. Peso de ", end='')
for pessoa in cadastros:
    if pessoa[1] == mais_pesado:
        print(f"{pessoa[0]}")
print(f"\nO mesor peso é {mais_leve}kg. Peso de ", end='')
for pessoa in cadastros:
    if pessoa[1] == mais_leve:
        print(f"{pessoa[0]}")
print(f"\nForam cadastradas {len(cadastros)} pessoas")
