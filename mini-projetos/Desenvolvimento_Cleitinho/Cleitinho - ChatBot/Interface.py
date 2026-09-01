import os
import threading
import customtkinter as ctk
import speech_recognition as sr 
from rich.traceback import install
from dotenv import load_dotenv
from groq import Groq

install()
load_dotenv() # Carrega as variáveis do ficheiro .env
chave_api = os.getenv("GROQ_API_KEY")

# Configurações globais
# Define o modo de aparencia da inteeface ("dark", "light", ou "system" que alinha ao modo do sistema)
ctk.set_appearance_mode("system") 
ctk.set_default_color_theme("dark-blue") # Opcioal, podemos escolher dentre 3 temas ("blue", "dark-blue", "green"), por padrão o tema é "blue"

# Instanciamos a janela
class MeuApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.historico_mensagens = [
            {"role": "system", "content": f"Seu nome é Cleitinho, um assistente pessoal"}]
        self.title("Cleitinho (ChatBot)")
        self.geometry("800x600") # Tamanho Inicial
        self.minsize(500,400) #Tamanho Minimo

        # Configurando Grid
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

        # ---- Caixa de texto Chat ----
        self.caixa_chat = ctk.CTkTextbox(self, font=("Consolas", 14), width=500, height=300, corner_radius=15)
        # Ocupa as lihas 0 e 1 (columnspan=2) e estica para todos os lados (stick="nsew")
        self.caixa_chat.grid(row=0, column=0, columnspan=2, padx=20, pady=(10, 20), stick="nsew")
        self.caixa_chat.insert("0.0", "Olá, eu sou o Cleitinho. Como posso te ajudar?\n\n")
        self.caixa_chat.configure(state="disabled")

        # ---- Barra de Pesquisa ----
        self.entrada_texto = ctk.CTkEntry(self, placeholder_text="Faça uma pergunta", corner_radius=30, width=500, height=40)
        self.entrada_texto.grid(row=1, column=0, columnspan=2, padx=20, pady=(0,20), stick="nsew")

        # --- Frame botões ----
        self.frame_botoes = ctk.CTkFrame(self, fg_color="transparent")
        self.frame_botoes.grid(row=1, column=1, padx=(1, 20), pady=(1,20), stick="e")

        # ---- Botões ----
        self.botao_enviar = ctk.CTkButton(self.frame_botoes, text="Enviar", width=30, corner_radius=30, fg_color="#005D96", hover_color="#009DE1", command=self.enviar_mensagem)
        self.botao_falar = ctk.CTkButton(self.frame_botoes, text=" Falar", width=30, corner_radius=30, fg_color="#005D96", hover_color="#009DE1", command=self.iniciar_fala)
        self.botao_enviar.pack(side="left", padx=5)
        self.botao_falar.pack(side="left", padx=5)
 
    # ---- Callbacks dos botões ----
    def adicionar_texto_chat(self, autor, mensagem):
        self.caixa_chat.configure(state="normal") # Desbloqueia para poder adicionar texto
        self.caixa_chat.insert("end", f"{autor}:\n{mensagem}\n\n")
        self.caixa_chat.see("end") # Faz o scroll descer automaticamente
        self.caixa_chat.configure(state="disabled") # Bloqueia novamente


    def enviar_mensagem(self):
        self.bloquear_botoes()
        mensagem_entrada = self.entrada_texto.get().strip()
        if mensagem_entrada:
            self.adicionar_texto_chat("Você", mensagem_entrada) # Exibe o que foi digitado
            self.entrada_texto.delete(0, "end") # Limpa da caixa de entrada
            threading.Thread(target=self.cleitinho, args=(mensagem_entrada,)).start()
        else:
            self.desbloquear_botoes()
        

    def capturar_fala(self):
        rec = sr.Recognizer()
        # O padrão é 0.8 segundos. Para almentar usamos ".pause_threshold" que recebe 1.5
        rec.pause_threshold = 1.5
        with sr.Microphone() as mic:
            rec.adjust_for_ambient_noise(mic)
            try:
                audio = rec.listen(mic, timeout=5) 
                mensagem_entrada = rec.recognize_google(audio, language="pt-BR")
            except sr.UnknownValueError:
                self.adicionar_texto_chat("Cleitinho:", "Desculpe, não consegui entender o áudio. Tente novamente.")
                self.desbloquear_botoes()
            except sr.WaitTimeoutError:
                self.adicionar_texto_chat("Cleitinho", "Nenhuma voz detectada. O microfone foi desligado por inatividade.")
                self.desbloquear_botoes()
            else:
                self.adicionar_texto_chat("Você", mensagem_entrada)
                threading.Thread(target=self.cleitinho, args=(mensagem_entrada,)).start()
    
                
    def iniciar_fala(self):
        self.bloquear_botoes()
        threading.Thread(target=self.capturar_fala).start()
        

    # Funções Auxiliares
    def bloquear_botoes(self):
        self.botao_enviar.configure(state="disabled")
        self.botao_falar.configure(state="disabled")
    
    def desbloquear_botoes(self):
        self.botao_enviar.configure(state="normal")
        self.botao_falar.configure(state="normal")
        

    def cleitinho(self, mensagem_entrada):
        chave_api = os.getenv("GROQ_API_KEY")
        # Verifica se o .env esta configurado corretamente
        if not chave_api:
            self.adicionar_texto_chat("Cleitinho", "ERRO: Chave da API do Groq não encontrada!")
            exit()
        
        cliente = Groq(api_key=chave_api)

        try:
            # Adiciona a pergunta atual ao histórico ANTES de chamar a API
            self.historico_mensagens.append({"role": "user", "content": mensagem_entrada})
            resposta = cliente.chat.completions.create(
                messages=self.historico_mensagens,
                model="llama-3.1-8b-instant"
            )
            resposta_cleitinho = resposta.choices[0].message.content
            # Guarda a resposta da IA no histórico com a role 'assistant' para o próximo turno
            self.historico_mensagens.append({"role": "assistant", "content": resposta_cleitinho})

        except Exception as e:
            aviso = (f"\n ---- ERRO DESCONHECIDO NA API: ---- \n{str(e)}")
            print(aviso)
            self.botao_enviar.configure(state="normal")
            self.botao_falar.configure(state="normal")
        else:
            self.adicionar_texto_chat("Cleitinho", resposta_cleitinho)
        finally:
            self.desbloquear_botoes()
