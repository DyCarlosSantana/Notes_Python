import os
from dotenv import load_dotenv
from rich.traceback import install
from rich.console import Console
from rich.panel import Panel
from groq import Groq

install()
load_dotenv() # Carrega as variáveis do ficheiro .env

console = Console()
chave_api = os.getenv("GROQ_API_KEY")

# Verifica se o .env esta configurado corretamente
if not chave_api:
    aviso = ("\n[bold red]❌ ERRO: Chave da API do Groq não encontrada![/bold red]")
    painel_aviso_falha = Panel(aviso, title="AVISO", border_style="red", width=80)
    console.print(painel_aviso_falha)
    exit()

cliente = Groq(api_key=chave_api)
historico_mensagens = []

while True:
    try:
        pergunta = input("\nPode perguntar: ").strip()
        if pergunta == "sair":
            break

        # Adiciona a pergunta atual ao histórico ANTES de chamar a API
        historico_mensagens = [{"role": "user", "content": pergunta}]
        resposta = cliente.chat.completions.create(
            messages=historico_mensagens,
            model="llama-3.1-8b-instant"
        )

        resposta_da_ia = resposta.choices[0].message.content
        # Guarda a resposta da IA no histórico com a role 'assistant' para o próximo turno
        historico_mensagens.append({"role": "assistent", "content": resposta_da_ia})

        painel_resposta = Panel(resposta_da_ia, title="Resposta (Groq):", subtitle="Digite 'sair' para encerrar a sessão", border_style="green", width=80)
        console.print(painel_resposta)

    except Exception as e:
        aviso = (f"\n[bold red]❌ ERRO DESCONHECIDO NA API:[/bold red]\n{str(e)}")
        painel_aviso_falha = Panel(aviso, title="AVISO", border_style="red", width=80)
        console.print(painel_aviso_falha)