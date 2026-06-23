# Desafio 19
"""
    Desafio 19: Simulador de Leitura de Livro
    O que fazer: Crie uma classe chamada Livro que simule a leitura de uma obra.
    No construtor, defina o titulo, total_paginas e inicialize a pagina_atual em 0.
    Crie um método chamado avancar_pagina(qtd) que permita ao leitor avançar um número específico de páginas.
    O sistema deve validar os limites: não é possível avançar além do número total de páginas do livro. Se o leitor chegar à última página, exiba uma mensagem estilizada informando que ele concluiu a leitura.
"""
from rich.console import Console
from rich.panel import Panel
from rich import print
from rich.traceback import install
install()

class Livro:
    def __init__(self, titulo, total_paginas, pagina_atual=1):
        self.titulo = titulo
        self.total_paginas = total_paginas
        self.pagina_atual = pagina_atual

        print(f":open_book: Você acabou de abrir o livro [cyan]{self.titulo}[/] que tem [yellow]{self.total_paginas} paginas[/] no total. Você esta na [yellow] pagina {self.pagina_atual}[/]")

    def avancar_pagina(self, avancar):
        try:
            if self.pagina_atual + avancar > self.total_paginas:
                return f'O número excede o total de paginas do livro "{self.titulo}"'
            else:
                self.pagina_atual += avancar
                if self.pagina_atual == self.total_paginas:
                    return f'Leitura de "{self.titulo}" finalizada!'
                else:
                    return f"Pagina atual atualizada: {self.pagina_atual}"
        except TypeError:
            return "Digite um NÚMERO do tipo inteiro"
        

livro01 = Livro("Filhos do Éden", 473)
print(livro01.avancar_pagina(5))