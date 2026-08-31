import sys

if len(sys.argv) == 2: # Lista de argumentos na linha de comando
    try: 
        caminho = sys.argv[1]
        with open(caminho, "r", encoding="utf-8") as f:
            print(f.read())

    except FileNotFoundError:
        print(f"Erro: arquivo '{caminho}' não encontrado.")
        sys.exit(1)
        
else:
    print(f"Erro: Sem argumentos repassados \nUso: python {sys.argv[0]} <caminho>")
    sys.exit(1)