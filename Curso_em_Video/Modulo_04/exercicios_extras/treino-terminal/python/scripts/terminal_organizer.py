"""
    Criar a pasta bagunca.
    Criar 10 arquivos com extensões variadas:
    1 .txt (ex: nota1.txt, nota2.txt, nota3.txt)
    2 .py (ex: script1.py, script2.py, script3.py)
    3 .jpg (ex: foto1.jpg, foto2.jpg)
    4 .csv (ex: dados1.csv, dados2.csv)

    Criar subpastas: textos/, scripts/, imagens/, dados/.
    Mover os arquivos para as pastas corretas usando curingas (mv *.txt textos/, etc.).
"""

import os

path = os.path("treino-terminal/python/bagunca")

if path is None:
    print("Caminho não Informado!")
    
try:
    for file in path:
        with open(path, "+a", encoding="utf-8") as f:
            nome = f.name()
            print(nome)
        
except Exception as erro:
    print(f"Erro: {erro.__class__}")