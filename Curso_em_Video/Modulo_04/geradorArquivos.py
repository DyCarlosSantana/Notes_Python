import os

# Defininfo o caminho
diretorio = 'desafios' #sempre alterar o diretorio para novos exercicios
# Cria o diretorio/pasta caso não exista
if not os.path.exists(diretorio):
    os.makedirs(diretorio)
    print("Novo diretorio criado")

# Define a quantidade de arquivos e o prefixo
quantidade = 22
prefixo = "desafio"

for i in range(16, quantidade + 1):
    nome_arquivo = f"{prefixo}_{i}.py"
    caminho = os.path.join(diretorio, nome_arquivo)
    with open(caminho, "w", encoding="utf-8") as f:
        f.write(f"# Desafio {i}\n")
    print(f"Criado: {nome_arquivo} em {diretorio}")

