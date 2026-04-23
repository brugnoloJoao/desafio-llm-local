# Desafio Final (usando uma IDE):
# 1- Carregar um arquivo .txt, onde cada linha será um elemento de uma lista do Python

# 2- Mandá-la ao modelo que você está rodando localmente para extrair, em formato JSON, onde cada item terá "usuario", "resenha original", "resenha_pt", "avaliacao" (Positiva, Negativa, Neutra)

# 3- Transformar a resposta do modelo em uma lista de dicionários Python

# 4- Criar uma função que, dada uma lista de dicionários, percorre a lista faz 2 coisas:
# a) conta a quantidade de avaliações positivas, negativas e neutras;
# b) une cada item dessa lista em uma variável do tipo string com algum separador.
# Ao final, retorna ambas as coisas.

from openai import OpenAI
from collections import Counter
from typing import List, Dict
import json

content = []
with open("Resenhas_App_ChatGPT.txt", "r", encoding="utf-8") as f:
    for line in f:
        content.append(line.strip().replace("$","$$$$$"))

client_openAI = OpenAI(
    base_url="http://127.0.0.1:1234/v1",
    api_key="lm-studio"    
)

response = client_openAI.chat.completions.create(
    model = "google/gemma-3-1b",
    messages= [
        {"role":"system", "content":"Você é um analista de dados e tradutor."},
        {"role":"user", 
        "content":
            f'''Vou te passar muitas resenhas, em diversas línguas diferentes, sobre análises do aplicativo do ChatGPT, separadas por "######", cada resenha possuí id, usuario e conteúdo (esses atributos estão separados por "$$$$$").
            Você deve enviar em formato JSON contendo todas as resenhas, cada item terá "usuario" (que corresponde ao NOME do usuário que enviou aquela resenha), "resenha_original" (que é o conteúdo enviado por aquele usuário sem NENHUMA alteração), "resenha_pt_br" (que a tradução da "resenha_original" para o português brasileiro), "avaliacao" (em que você deve analisar se as emoções do conteúdo da resenha e classificalas utilizando APENAS uma dentre essas 3 palavras: Positiva, Negativa, Neutra)

            Aqui estão as resenhas: {"######".join(content)}
            Retorne APENAS o arquivo JSON.'''
        }, 
    ],
    temperature=1.0
)

response_json = json.loads(response.choices[0].message.content.replace("json", "").replace("```", ""))

def process_reviews(review_list: List[Dict]):

    summarize_reviews = dict(Counter(emotion["avaliacao"] for emotion in review_list))

    reviews_in_text =  "|||||".join(str(item) for item in review_list)

    return summarize_reviews, reviews_in_text

summarize_reviews, reviews_in_text = process_reviews(response_json)

print(summarize_reviews)
print(reviews_in_text)
