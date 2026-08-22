# 🐍 Notes_Python

> Repositório pessoal de estudos, anotações e projetos práticos em Python — construído ao longo da jornada de aprendizado, do básico à orientação a objetos e integrações com APIs externas.

---

## 🎯 Sobre o repositório

Este repositório funciona como um **caderno de estudos**: reúne exercícios, desafios e pequenos projetos desenvolvidos durante cursos e práticas autônomas em Python. Não é um tutorial nem uma biblioteca pronta para uso — é o registro da evolução técnica, desde lógica de programação até tópicos mais avançados como orientação a objetos, manipulação de arquivos, automação e integração com APIs.

Por natureza, o conteúdo **cresce e muda com frequência**: novas aulas, desafios e projetos são adicionados continuamente conforme o aprendizado avança. Por isso, este README descreve a *estrutura e o propósito* de cada área, em vez de listar arquivos específicos — assim ele continua válido mesmo quando novo conteúdo é incluído.

---

## 📁 Estrutura geral

O repositório é organizado em três grandes frentes de estudo:

### `Curso_em_Video/`
Acompanhamento do curso completo de Python do **Curso em Vídeo** (prof. Gustavo Guanabara), organizado por módulos progressivos (`Modulo_01`, `Modulo_02`, ...). Cada módulo contém as aulas correspondentes e os desafios propostos, cobrindo uma trilha que vai de lógica básica (variáveis, condições, repetições) até tópicos intermediários/avançados (funções, manipulação de arquivos, bibliotecas de terceiros como `rich`, boas práticas de estrutura de projeto).

### `Hashtag/`
Exercícios e mini-projetos baseados em conteúdos da **Hashtag Programação**, com foco em aplicações práticas e automações do dia a dia — como conversão de arquivos, reconhecimento de fala, validação de documentos (CPF/CNPJ) e automação de interface via teclado/mouse.

### `mini-projetos/`
Projetos autorais e independentes, não vinculados a nenhum curso específico. É aqui que ideias próprias são colocadas em prática — incluindo o **Cleitinho**, um chatbot em desenvolvimento com integração à API da Groq, reconhecimento de fala e interface gráfica própria.

> 💡 Como cada pasta cresce de forma independente, o número de módulos, aulas e projetos dentro de cada categoria não é fixo — a divisão acima representa a *lógica de organização*, que se mantém estável mesmo quando novos itens são adicionados.

---

## 🛠️ Tecnologias e bibliotecas

O núcleo do repositório é **Python puro**, mas diversos exercícios e projetos exploram bibliotecas externas, entre elas:

| Categoria | Bibliotecas observadas |
|---|---|
| Interface e output no terminal | `rich`, `colorama` |
| Integração com APIs / IA | `groq`, `python-dotenv` |
| Reconhecimento de fala e áudio | `speech_recognition`, `pygame` |
| Automação | `pyautogui`, `keyboard` |
| Validação de dados | `validate-docbr` |

Essa lista tende a se expandir conforme novos projetos são adicionados — não deve ser tratada como exaustiva.

---

## 🧭 Como navegar

- **Para acompanhar a evolução cronológica do aprendizado:** comece por `Curso_em_Video/Modulo_01` e avance pelos módulos em ordem.
- **Para ver aplicações práticas e scripts pontuais:** explore `Hashtag/`.
- **Para ver projetos mais elaborados e autorais:** vá direto a `mini-projetos/`.

Cada pasta de aula ou projeto é autocontida — em geral, basta abrir o arquivo `.py` principal daquela pasta para entender o exercício, sem dependências entre pastas diferentes (exceto quando um projeto usa módulos próprios, como em `Cleitinho - ChatBot/`).

---

## ⚙️ Executando os scripts

A maioria dos arquivos é independente e pode ser executada diretamente:

```bash
python nome_do_arquivo.py
```

Para os projetos que dependem de bibliotecas externas (como o Cleitinho, que usa `groq` e `python-dotenv`), recomenda-se criar um ambiente virtual e instalar as dependências indicadas nos imports do próprio arquivo antes de rodar:

```bash
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install <biblioteca-necessária>
```

Alguns projetos que utilizam chaves de API (como o Cleitinho) esperam um arquivo `.env` local — que não é versionado por questões de segurança.

---

## 📜 Licença

Este repositório está sob a licença **MIT** — veja o arquivo [`LICENSE`](./LICENSE) para mais detalhes.

---

## ✍️ Autor
**Edy Carlos de Santana Souza**
[GitHub: @DyCarlosSantana](https://github.com/DyCarlosSantana)
