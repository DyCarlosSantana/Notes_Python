import os

# Defininfo o caminho
diretorio = 'Aula_23' #sempre alterar o diretorio para novos exercicios
# Cria o diretorio/pasta caso não exista
if not os.path.exists(diretorio):
    os.makedirs(diretorio)
    print("Novo diretorio criado")

# Define a quantidade de arquivos e o prefixo
quantidade = 112
prefixo = "exercicio"

for i in range(107, quantidade + 1):
    nome_arquivo = f"{prefixo}_{i}.py"
    caminho = os.path.join(diretorio, nome_arquivo)
    with open(caminho, "w", encoding="utf-8") as f:
        f.write(f"# Este é o arquivo número {i}\n")
    print(f"Criado: {nome_arquivo} em {diretorio}")

