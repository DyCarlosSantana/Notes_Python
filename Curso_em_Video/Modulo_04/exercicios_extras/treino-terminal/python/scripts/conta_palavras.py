"""
Crie outro script chamado conta_palavras.py que recebe um nome de arquivo e imprime:
- Número de linhas
- Número de palavras
- Número de caracteres

Dicas:
- Linhas: conteudo.splitlines()
- Palavras: conteudo.split()
- Caracteres: len(conteudo)
"""

import sys

if len(sys.argv) == 2:
    try:
        caminho = sys.argv[1]
        
        with open(caminho, "r", encoding="utf-8") as f:
            conteudo = f.read()
           
        linhas = conteudo.splitlines()
        palavras = conteudo.split()
        caracteres = len(conteudo)
        
        print(f"Linhas: {len(linhas)} -> {linhas}")
        print(f"Palavras: {len(palavras)} -> {palavras}")
        print(f"Caracteres: {caracteres}")
        
    except FileNotFoundError:
            print(f"Erro: arquivo '{caminho}' não encontrado.")
            sys.exit(1)
else: 
    print(f"Erro: Sem argumentos repassados \nUso: python {sys.argv[0]} <caminho>")
    sys.exit(1)
        