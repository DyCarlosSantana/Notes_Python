# Nível 1 — você deve conseguir fazer sozinho:
# Crie uma lista com 5 nomes.
# Imprima apenas os nomes que têm mais de 4 letras.

nomes = ["Edy", "Bruna", "Carlos", "Beth"]
for nome in nomes:
    if len(nome) >= 4:
        print(nome)

# Nível 2 — você deve conseguir fazer com algum esforço:
# Crie uma lista com 10 números.
# Calcule a média deles.
# Imprima quantos números estão acima da média.
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
soma = sum(numeros)
media = soma / len(numeros)
print(f"A média é: {media}")
acima = 0
for num in numeros:
    if num > media:
        acima += 1
print(f"Números acima da média: {acima}")

# Nível 3 — se conseguir, está bem acima do esperado para aula #17:
# Crie uma lista de compras.
# Permita que o usuário adicione itens digitando no terminal.
# Quando digitar "sair", o programa para e imprime a lista final.

lista = []
compra = []
while True:
    compra.append(str(input("Item: ")))
    compra.append(int(input("Qtd: ")))
    lista.append(compra[:])
    compra.clear()

    print("---"*10)
    resp_usuario = str(input("Deseja Continuar [S/N]: "))
    print("---"*10)
    if resp_usuario.upper() == "N":
        break
print("==="*10)
print("LISTA DE COMPRAS")
print("==="*10)
for index, compra in enumerate(lista):
    print(f"{index}. {compra[0]} - {compra[1]}")