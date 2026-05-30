# 📊 Analisador e Tradutor de Resenhas com LLM Local

Este projeto é o **Desafio Final** de processamento de texto e integração com Modelos de Linguagem (LLMs). O objetivo é ler um arquivo de resenhas de usuários sobre o aplicativo do ChatGPT, utilizar um modelo de IA rodando localmente para traduzir e classificar o sentimento dessas resenhas, e extrair métricas consolidadas a partir dos dados estruturados.

---

## 🎯 Objetivos do Desafio

1. **Carga de Dados:** Ler um arquivo `.txt` contendo avaliações e converter cada linha em um elemento de uma lista Python.
2. **Integração com LLM (Local):** Enviar os dados para um modelo local (via LM Studio) solicitando uma resposta estritamente formatada em **JSON**.
3. **Extração de Informações:** Obter do modelo os campos: `usuario`, `resenha_original`, `resenha_pt_br` e `avaliacao` (Positiva, Negativa ou Neutra).
4. **Estruturação:** Converter a string JSON retornada pela IA em uma lista de dicionários Python.
5. **Análise e Agregação:** Criar uma função para:
   - Contar a quantidade de avaliações por sentimento (Positiva, Negativa, Neutra).
   - Unificar todas as resenhas estruturadas em uma única string com um separador customizado (`|||||`).

---

## 🛠️ Tecnologias e Ferramentas

* **Python 3.x**
* **OpenAI SDK Python** (utilizado para comunicação com a API local)
* **LM Studio** (para servir o modelo localmente)
* **Modelo Utilizado:** `google/gemma-3-1b` (ou qualquer outro de sua escolha configurado no LM Studio)

---

## 📋 Pré-requisitos & Configuração

### 1. LM Studio (Servidor Local)
Para que o código funcione, você precisa ter o **LM Studio** instalado e rodando em sua máquina:
1. Baixe o modelo `google/gemma-3-1b` (ou similar) pelo LM Studio.
2. Vá até a aba **Local Server** (ícone de setas/servidor na lateral).
3. Certifique-se de que a porta configurada é a `1234` (URL base: `http://127.0.0.1:1234/v1`).
4. Clique em **Start Server**.

### 2. Arquivo de Dados
O código espera um arquivo chamado `Resenhas_App_ChatGPT.txt` no mesmo diretório do script. O formato esperado para cada linha/resenha deve conter as informações separadas por cifrões (que o código internamente trata e escapa).

### 3. Instalação de Dependências
Instale a biblioteca oficial da OpenAI para Python:

```bash
pip install openai
