from rich import print

# Cores e estilo de texto: Permite usar tags para colorir e estilizar o texto similar ao html

# CORES: red, green, blue, yellow, magenta, cyan, white, black
# CORES DE FUNDO: red, green, blue, yellow, magenta, cyan, white, black
print("Olá, [red]mundo![/red]") # [/red] ou apenas [/] para fechar a tag
print("Olá, [red on white]mundo![/red on white]") # usar a palavra "on" para indicar a cor de fundo

# ESTILOS: bold, italic, underline, reverse, dim, blink
print("Olá, [bold]mundo![/bold]")

# EMOJI: Permite usar emojis usando a sintaxe :emoji_name, usando a biblioteca emoji para listar os emojis disponíveis (python -m rich.emoji):
#Juntando tudo:
print("Olá, [red bold]mundo![/red bold] :smile:")

# Painel: Permite criar painéis com bordas e títulos
from rich.panel import Panel
panel = Panel("Este é um painel", title="Título do Painel", border_style="red")
print(panel)
"""
Outros recursos do Painel:
- Estilo de borda: border_style="red" (red, green, blue, yellow, magenta, cyan, white, black)
- Título: title="Título do Painel"
- Alinhamento do título: title_align="center" (left, center, right)
"""

# Tabelas: Permite criar tabelas formatadas
from rich.table import Table
table = Table()
table.add_column("Nome")
table.add_column("Idade")
table.add_row("Alice", "25")
table.add_row("Bob", "30")
print(table)
"""
Outros recursos da tabela:
- Alinhamento: table.add_column("Nome", justify="center") (left, center, right)
- Estilo de borda: table.border_style = "red" (red, green, blue, yellow, magenta, cyan, white, black)
- Título: table.title = "Título da Tabela"
- Cabeçalho: table.show_header = True (True, False)
- Linhas de grade: table.show_lines = True (True, False)
- Colunas de largura fixa: table.add_column("Nome", width=20)
- Colunas de largura mínima: table.add_column("Nome", min_width=10)
- Colunas de largura máxima: table.add_column("Nome", max_width=30)
- Colunas de largura proporcional: table.add_column("Nome", ratio=1)
- Colunas de largura automática: table.add_column("Nome", no_wrap=True)
- Colunas de largura automática com quebra de linha: table.add_column("Nome", no_wrap=False)
"""

# Painel com tabela dentro
panel = Panel(table, title="Tabela no Painel", border_style="green")
print(panel)
"""
Outros recursos do Painel:
- Estilo de borda: border_style="red" (red, green, blue, yellow, magenta, cyan, white, black)
- Título: title="Título do Painel"
- Alinhamento do título: title_align="center" (left, center, right)
"""

# Markdown: Permite renderizar texto em formato markdown
from rich.markdown import Markdown
markdown = Markdown("# Título\n\nEste é um texto em **markdown** com *itálico* e `código`.")
print(markdown)
"""
Outros recursos do metodo markdown:
# Título 1
## Título 2
### Título 3
**Texto em negrito**
*Texto em itálico*
`Código em linha`
```python
    # Bloco de código
    print("Olá, mundo!")
```
- Listas:
- Item 1 
- Item 2
- Item 3
"""
# Renderização de JSON: Permite renderizar dados em formato JSON de forma formatada
from rich.json import JSON
json_data = '{"nome": "Alice", "idade": 25, "cidade": "São Paulo"}'
json_rendered = JSON(json_data)
print(json_rendered)
"""
Outros recursos do metodo JSON:
- Formatação: JSON(json_data, indent=2) Permite definir a indentação para melhorar a legibilidade do JSON
- Destaque de sintaxe: JSON(json_data, syntax_highlight=True) Permite destacar a sintaxe do JSON para facilitar a leitura
"""

# Renderização de código-fonte: Permite renderizar código-fonte com destaque de sintaxe
from rich.syntax import Syntax
code = '''def saudacao(nome):
    return f"Olá, {nome}!"'''
syntax_rendered = Syntax(code, "python", theme="monokai")
print(syntax_rendered)
"""
Outros recursos do metodo Syntax:
- Linguagem: Syntax(code, "python") Permite especificar a linguagem do código para aplicar o destaque de sintaxe correto
- Tema: Syntax(code, "python", theme="monokai")...
    Permite escolher um tema de cores para o destaque de sintaxe (monokai, dracula, solarized-dark, solarized-light, etc.)
- Linhas numeradas: Syntax(code, "python", line_numbers=True) Permite exibir números de linha ao lado do código para facilitar a referência
"""

# Progresso: Permite criar barras de progresso para acompanhar o andamento de tarefas
from rich.progress import Progress
with Progress() as progress:
    task1 = progress.add_task("[red]Processando...", total=100)
    task2 = progress.add_task("[green]Carregando...", total=100)
    
    while not progress.finished:
        progress.update(task1, advance=0.5)  # Avança a tarefa 1
        progress.update(task2, advance=0.3)  # Avança a tarefa 2
"""
Outros recursos do metodo Progress:
- Tarefas: progress.add_task("[red]Processando...", total=100) Permite adicionar tarefas com um título e um total de progresso
- Atualização: progress.update(task1, advance=0.5) Permite atualizar o progresso de uma tarefa específica, avançando um valor específico
- Personalização: Progress(transient=True) Permite personalizar a aparência da barra de progresso, como cor, estilo e formato
"""

# Traceback: Permite exibir tracebacks de erros de forma formatada
from rich.traceback import install
install()  # Instala o manipulador de tracebacks do Rich
def funcao_que_gera_erro():
    return 1 / 0  # Isso vai gerar um erro de divisão por zero
funcao_que_gera_erro()
"""
Outros recursos do metodo Traceback:
- Instalação: install() Permite instalar o manipulador de tracebacks do Rich para exibir erros de forma formatada
- Personalização: install(show_locals=True) Permite incluir variáveis locais no traceback para facilitar a depuração
- Integração: O Rich Traceback pode ser integrado com frameworks de teste como pytest para melhorar a exibição de erros durante os testes
"""

# Inspeção de objetos: Permite inspecionar objetos Python de forma formatada
from rich import inspect
class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

pessoa = Pessoa("Alice", 30)
inspect(pessoa)
"""
Outros recursos do metodo inspect:
- Inspeção de objetos: inspect(pessoa) Permite inspecionar um objeto Python, exibindo seus atributos e métodos de forma formatada
- Personalização: inspect(pessoa, methods=True) Permite incluir os métodos do objeto na inspeção para obter uma visão mais completa do objeto
- Profundidade: inspect(pessoa, depth=2) Permite definir a profundidade da inspeção para objetos aninhados, controlando o nível de detalhes exibidos
"""

# Console: Permite criar consoles personalizados para exibir mensagens formatadas
from rich.console import Console
console = Console()
console.print("Olá, [bold magenta]mundo![/bold magenta]")
"""
Outros recursos do metodo Console:
- Impressão formatada: console.print("Olá, [bold magenta]mundo![/bold magenta]") Permite imprimir mensagens formatadas usando tags de estilo e cor
- Personalização: Console(color_system="windows") Permite personalizar o console, como definir o sistema de cores para compatibilidade com diferentes terminais
- Integração: O Console do Rich pode ser integrado com outras bibliotecas para exibir mensagens formatadas em diferentes contextos, como logs, testes e interfaces de linha de comando
"""
